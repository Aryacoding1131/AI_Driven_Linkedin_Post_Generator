@echo off
title AI LinkedIn Post Generator

REM Go to the folder where this BAT file is located
cd /d "%~dp0"

echo ==========================================
echo    AI LinkedIn Post Generator
echo ==========================================
echo.

REM Activate virtual environment
call ".env\Scripts\activate.bat"

REM Check if activation worked
if errorlevel 1 (
    echo.
    echo ERROR: Could not activate virtual environment.
    pause
    exit /b
)

echo Virtual environment activated.
echo Starting Streamlit...
echo.

REM Start Streamlit
python -m streamlit run app.py

echo.
echo Application closed.
pause
