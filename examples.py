"""
Example code files for testing the compiler
"""

SIMPLE_PROGRAM = """
main() {
    int x;
    x = 42;
    print("Hello World", x);
}
"""

FUNCTION_PROGRAM = """
int soma(int a, int b) {
    return a + b;
}

main() {
    int resultado;
    resultado = func soma(10, 20);
    println("Resultado:", resultado);
}
"""

COMPLEX_PROGRAM = """
int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return func fibonacci(n-1) + func fibonacci(n-2);
}

main() {
    int i;
    for (i = 0; i < 10; i = i + 1) {
        println("fib(", i, ") = ", func fibonacci(i));
    }
}
"""