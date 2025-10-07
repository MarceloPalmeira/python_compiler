#!/bin/bash

# Script to generate ANTLR Python files
# Make sure you have antlr4-tools installed: pip install antlr4-tools

echo "Generating ANTLR Python files..."

cd grammar

# Generate Python files from ANTLR grammar
antlr4 -Dlanguage=Python3 -visitor -listener LexerGrammar.g4 ParserGrammar.g4

# Create generated directory if it doesn't exist
mkdir -p ../compiler/generated

# Move generated files to appropriate directory
mv *.py ../compiler/generated/ 2>/dev/null || true
mv *.tokens ../compiler/generated/ 2>/dev/null || true
mv *.interp ../compiler/generated/ 2>/dev/null || true

# Create __init__.py in generated directory
touch ../compiler/generated/__init__.py

cd ..

echo "ANTLR files generated successfully!"
echo "Generated files are in compiler/generated/"