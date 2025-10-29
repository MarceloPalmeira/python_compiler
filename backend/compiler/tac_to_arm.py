
"""Canonical functional TAC -> ARM translator.

This module provides a small, well-scoped translator and stable API
`tac_to_arm(tac: List[str]) -> str` that the service can call. It is a
single, self-contained functional implementation (no classes).

Small functional translator that converts a list of TAC lines (strings)
into a single ARM assembly string. It is intentionally simple and
suitable for the project's tests/CPULator runtime.
"""

from typing import List
import re


def tac_to_arm(tac: List[str]) -> str:
    """Translate TAC (list of strings) into an ARM-like assembly string.

    Implementation notes:
    - r0..r3: arg/return registers
    - r4..r11: temporaries
    - r12: spill register
    - params are buffered until a following call consumes them
    - prologue: push {r4-r11, lr}; epilogue: pop {r4-r11, pc}
    """

    asm_lines: List[str] = []
    reg_map = {}
    next_reg = 4
    param_buffer: List[str] = []
    in_function = False
    function_returned = False

    def alloc_reg(name: str) -> str:
        nonlocal next_reg
        if name in reg_map:
            return reg_map[name]
        if next_reg < 12:
            r = f"r{next_reg}"
            reg_map[name] = r
            next_reg += 1
            return r
        reg_map[name] = 'r12'
        return 'r12'

    def emit(line: str) -> None:
        asm_lines.append(line)

    # header
    emit('.text')
    emit('.global _start')
    emit('')
    emit('_start:')

    for instr in tac:
        instr = instr.strip()
        if not instr:
            continue
        if instr.startswith(';'):
            emit(f"    @ {instr[1:].strip()}")
            continue

        # param X -> buffer until a call
        m = re.match(r'^param\s+(.*)$', instr)
        if m:
            param_buffer.append(m.group(1))
            continue

        # call (with optional assignment)
        m_assign_call = re.match(r'^(\w+)\s*=\s*call\s+(\w+)\s*,\s*(\d+)$', instr)
        m_call = re.match(r'^call\s+(\w+)\s*,\s*(\d+)$', instr)
        if m_assign_call or m_call:
            if m_assign_call:
                target, fname, argc = m_assign_call.group(1), m_assign_call.group(2), int(m_assign_call.group(3))
            else:
                target, fname, argc = None, m_call.group(1), int(m_call.group(2))

            # move up to 4 args into r0..r3
            for i in range(min(argc, 4)):
                if i >= len(param_buffer):
                    break
                val = param_buffer[i]
                if val.replace('-', '').isdigit():
                    emit(f"    mov r{i}, #{val}")
                else:
                    rs = alloc_reg(val)
                    emit(f"    mov r{i}, {rs}")

            # push extra args on stack (right-to-left)
            if argc > 4:
                for j in range(argc - 1, 3, -1):
                    if j >= len(param_buffer):
                        break
                    v = param_buffer[j]
                    if v.replace('-', '').isdigit():
                        emit(f"    mov r12, #{v}")
                        emit(f"    push {{r12}}")
                    else:
                        rv = alloc_reg(v)
                        emit(f"    push {{{rv}}}")

            # perform call
            if fname == 'print':
                emit(f"    @ call print (placeholder), argc={argc}")
            else:
                emit(f"    bl {fname}")

            # cleanup pushed args
            if argc > 4:
                cleanup = (argc - 4) * 4
                emit(f"    add sp, sp, #{cleanup}    @ cleanup {argc-4} pushed args")

            # assignment from call
            if target:
                rd = alloc_reg(target)
                emit(f"    mov {rd}, r0     @ {target} = return")

            param_buffer = []
            continue

        # return
        m = re.match(r'^(?:return|ret)(?:\s+(.*))?$', instr)
        if m:
            val = m.group(1)
            if val:
                if val.replace('-', '').isdigit():
                    emit(f"    mov r0, #{val}")
                else:
                    rv = alloc_reg(val)
                    emit(f"    mov r0, {rv}")
            if in_function:
                emit(f"    pop {{r4-r11, pc}}")
                function_returned = True
            else:
                emit('')
                emit('    @ Exit program (return)')
                emit('    mov r7, #1')
                emit('    swi 0')
            continue

        # function start
        m = re.match(r'^func\s+(\w+)$', instr)
        if m:
            fname = m.group(1)
            emit(f"{fname}:")
            emit(f"    push {{r4-r11, lr}}")
            in_function = True
            function_returned = False
            # Save global register map and start fresh for function locals
            # Note: In a more sophisticated compiler, we'd handle scoping better
            continue

        # function end
        m = re.match(r'^endfunc\s+(\w+)$', instr)
        if m:
            if in_function and not function_returned:
                # Only emit pop if we haven't already returned
                emit(f"    pop {{r4-r11, pc}}")
            in_function = False
            function_returned = False
            continue

        # simple assignment or parameter mapping
        m = re.match(r'^(\w+)\s*=\s*(\w+|\d+|r\d+)(?:\s*;\s*param\s+\d+)?$', instr)
        if m:
            left, right = m.group(1), m.group(2)
            if right.startswith('r') and right[1:].isdigit():
                # Parameter mapping from register
                reg_map[left] = right
                emit(f"    @ {left} mapped to {right}")
            elif right.replace('-', '').isdigit():
                rd = alloc_reg(left)
                emit(f"    mov {rd}, #{right}     @ {left} = {right}")
            else:
                rs = alloc_reg(right)
                rd = alloc_reg(left)
                emit(f"    mov {rd}, {rs}     @ {left} = {right}")
            continue

        # binary op
        m = re.match(r'^(t\d+)\s*=\s*(\w+)\s*([+\-*/])\s*(\w+|\d+)$', instr)
        if m:
            tmp, a, op, b = m.group(1), m.group(2), m.group(3), m.group(4)
            if a.replace('-', '').isdigit():
                ra = alloc_reg(f"_lit_{a}")
                emit(f"    mov {ra}, #{a}")
            else:
                ra = alloc_reg(a)

            if b.replace('-', '').isdigit():
                rb = alloc_reg(f"_lit_{b}")
                emit(f"    mov {rb}, #{b}")
            else:
                rb = alloc_reg(b)

            rt = alloc_reg(tmp)
            if op == '+':
                emit(f"    add {rt}, {ra}, {rb}     @ {tmp} = {a} + {b}")
            elif op == '-':
                emit(f"    sub {rt}, {ra}, {rb}     @ {tmp} = {a} - {b}")
            elif op == '*':
                emit(f"    mul {rt}, {ra}, {rb}     @ {tmp} = {a} * {b}")
            else:
                emit(f"    @ div not implemented; mov {rt}, {ra}")
                emit(f"    mov {rt}, {ra}")
            continue

        # fallback
        emit(f"    @ unhandled TAC: {instr}")

    # epilogue
    emit('')
    emit('    @ Exit program (end)')
    emit('    mov r7, #1')
    emit('    mov r0, #0')
    emit('    swi 0')

    return '\n'.join(asm_lines)


def generate_arm_from_tac(tac: List[str]) -> str:
    """Alias function for backward compatibility."""
    return tac_to_arm(tac)
