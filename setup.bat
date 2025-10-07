@echo off
REM Setup script for Python Compiler (Windows)

echo ===================================
echo Setting up Python Compiler Project
echo ===================================

REM Check Python version
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo Using: 
python --version

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo Installing Python dependencies...
pip install -r requirements.txt

REM Install ANTLR4 tools
echo Installing ANTLR4 tools...
pip install antlr4-tools

REM Generate ANTLR files
echo Generating ANTLR Python files...
call generate_antlr.bat

echo.
echo =====================================
echo Setup completed successfully!
echo =====================================
echo.
echo To use the compiler:
echo 1. Activate the virtual environment:
echo    venv\Scripts\activate.bat
echo.
echo 2. Run the CLI:
echo    python main.py compiler --help
echo.
echo 3. Start the API:
echo    python main.py api
echo.
echo 4. Test with example:
echo    python main.py compiler test_simple.txt
echo.
echo Deactivate virtual environment when done:
echo    deactivate

pause