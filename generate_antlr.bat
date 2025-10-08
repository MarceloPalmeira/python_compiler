@echo off
REM Script to generate ANTLR Python files for Windows
REM Supports both original (legacy) and MiniPar grammars
REM Make sure you have antlr4-tools installed: pip install antlr4-tools

echo ==========================================
echo Generating ANTLR Python files for MiniPar
echo ==========================================

cd grammar

REM Generate Python files from original grammar (legacy syntax)
echo Generating original grammar files...
antlr4 -Dlanguage=Python3 -visitor -listener LexerGrammar.g4 ParserGrammar.g4

REM Create generated directory if it doesn't exist
if not exist "..\compiler\generated" mkdir "..\compiler\generated"

REM Move original generated files
move *.py ..\compiler\generated\ >nul 2>&1
move *.tokens ..\compiler\generated\ >nul 2>&1
move *.interp ..\compiler\generated\ >nul 2>&1

REM Create __init__.py in generated directory
echo # Generated ANTLR files for original grammar > ..\compiler\generated\__init__.py

REM Generate Python files from MiniPar grammar
echo Generating MiniPar grammar files...
antlr4 -Dlanguage=Python3 -visitor -listener LexerGrammarMinipar.g4 ParserGrammarMinipar.g4

REM Create generated_minipar directory if it doesn't exist
if not exist "..\compiler\generated_minipar" mkdir "..\compiler\generated_minipar"

REM Move MiniPar generated files
move *.py ..\compiler\generated_minipar\ >nul 2>&1
move *.tokens ..\compiler\generated_minipar\ >nul 2>&1
move *.interp ..\compiler\generated_minipar\ >nul 2>&1

REM Create __init__.py in generated_minipar directory
echo # Generated ANTLR files for MiniPar grammar > ..\compiler\generated_minipar\__init__.py

cd ..

echo =============================================
echo ANTLR files generated successfully!
echo =============================================
echo Generated files locations:
echo - Original grammar: compiler/generated/
echo - MiniPar grammar:  compiler/generated_minipar/
echo.
echo Note: The project primarily uses SimpleMiniparCompiler
echo (standalone implementation without ANTLR dependencies)
echo.
echo ANTLR files are available for advanced parsing if needed.