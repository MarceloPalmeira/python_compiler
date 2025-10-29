#!/usr/bin/env python3
"""
Projeto Compiladores - Python Version
CLI do projeto de Compiladores em Python
"""

import click
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))


@click.group()
@click.version_option("0.0.1")
def cli():
    """Projeto Compiladores - Python Version"""
    pass


@cli.command()
@click.argument('input_file', type=click.Path(exists=True), required=False)
@click.option('-o', '--out', '--outfile', 'output_file', type=click.Path(), 
              help='Specify the output file, if not set it will be sent to stdout')
@click.option('-t', '--show-tree', is_flag=True, 
              help='Display the parse tree')
def compiler(input_file, output_file, show_tree):
    """Compiles the code to TAC (three-address code)"""
    try:
        from compiler.compiler_command import CompilerCommand
        compiler_cmd = CompilerCommand()
        compiler_cmd.run(input_file, output_file, show_tree)
    except ImportError as e:
        print(f"Error: {e}")
        print("Please make sure the compiler module is properly installed.")
        print("Try running: pip install -r requirements.txt")
        sys.exit(1)


@cli.command()
@click.option('--host', default='127.0.0.1', help='Host to bind to')
@click.option('--port', default=8000, help='Port to bind to')
@click.option('--reload', is_flag=True, help='Enable auto-reload')
def api(host, port, reload):
    """Runs the API"""
    try:
        from api.main import run_api
        run_api(host=host, port=port, reload=reload)
    except ImportError as e:
        print(f"Error: {e}")
        print("Please make sure all dependencies are installed:")
        print("  pip install -r requirements.txt")
        sys.exit(1)


if __name__ == '__main__':
    cli()