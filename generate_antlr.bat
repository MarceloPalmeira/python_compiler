@echo off
REM Script to generate ANTLR Python files for Windows
REM Make sure you have antlr4-tools installed: pip install antlr4-tools

echo Generating ANTLR Python files...

cd grammar

REM Generate Python files from ANTLR grammar
antlr4 -Dlanguage=Python3 -visitor -listener LexerGrammar.g4 ParserGrammar.g4

REM Create generated directory if it doesn't exist
if not exist "..\compiler\generated" mkdir "..\compiler\generated"

REM Move generated files to appropriate directory
move *.py ..\compiler\generated\ >nul 2>&1
move *.tokens ..\compiler\generated\ >nul 2>&1
move *.interp ..\compiler\generated\ >nul 2>&1

REM Create __init__.py in generated directory
echo # Generated ANTLR files > ..\compiler\generated\__init__.py

cd ..

echo ANTLR files generated successfully!
echo Generated files are in compiler/generated/