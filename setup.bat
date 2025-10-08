@echo off
REM Setup script for MiniPar Compiler (Windows)

echo =============================================
echo Setting up MiniPar Compiler Project 2025.1
echo =============================================

REM Check Python version
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ and add to PATH
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

REM Generate ANTLR files (optional - using SimpleMiniparCompiler as primary)
echo Generating ANTLR files (optional)...
call generate_antlr.bat

echo.
echo ===============================================
echo MiniPar Compiler Setup completed successfully!
echo ===============================================
echo.
echo To use the MiniPar compiler:
echo.
echo 1. Activate the virtual environment:
echo    venv\Scripts\activate.bat
echo.
echo 2. Run CLI with MiniPar code:
echo    python main.py compiler exemplo.minipar
echo.
echo 3. Start the API server:
echo    python run_api.py
echo    or
echo    python main.py api
echo.
echo 4. Test with MiniPar examples:
echo    python main.py compiler test_minipar.minipar
echo    python comprehensive_test.py
echo.
echo 5. API Documentation:
echo    http://localhost:8000/docs
echo.
echo 6. CPULator ARM Emulator:
echo    https://cpulator.01xz.net/?sys=arm
echo.
echo Deactivate virtual environment when done:
echo    deactivate

pause