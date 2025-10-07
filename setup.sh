#!/bin/bash

# Setup script for Python Compiler

echo "==================================="
echo "Setting up Python Compiler Project"
echo "==================================="

# Check Python version
python_version=$(python3 --version 2>&1)
if [[ $? -ne 0 ]]; then
    echo "Error: Python 3 is not installed or not in PATH"
    exit 1
fi

echo "Using: $python_version"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Install ANTLR4 tools
echo "Installing ANTLR4 tools..."
pip install antlr4-tools

# Generate ANTLR files
echo "Generating ANTLR Python files..."
chmod +x generate_antlr.sh
./generate_antlr.sh

echo ""
echo "====================================="
echo "Setup completed successfully!"
echo "====================================="
echo ""
echo "To use the compiler:"
echo "1. Activate the virtual environment:"
echo "   source venv/bin/activate"
echo ""
echo "2. Run the CLI:"
echo "   python main.py compiler --help"
echo ""
echo "3. Start the API:"
echo "   python main.py api"
echo ""
echo "4. Test with example:"
echo "   python main.py compiler test_simple.txt"
echo ""
echo "Deactivate virtual environment when done:"
echo "   deactivate"