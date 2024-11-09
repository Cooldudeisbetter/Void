@echo off
setlocal enabledelayedexpansion

net session >nul 2>&1
if %errorlevel% neq 0 (
    echo This script requires administrator privileges. Please run it as Administrator.
    pause
    exit /b
)


set "DOWNLOAD_DIR=%TEMP%\setup_tools"
if not exist "%DOWNLOAD_DIR%" mkdir "%DOWNLOAD_DIR%"
cd /d "%DOWNLOAD_DIR%"

echo Installing Python...

set "PYTHON_VERSION=3.13.0"
set "PYTHON_INSTALLER=python-%PYTHON_VERSION%-amd64.exe"
set "PYTHON_URL=https://www.python.org/ftp/python/%PYTHON_VERSION%/%PYTHON_INSTALLER%"

echo Downloading Python from %PYTHON_URL%...
powershell -Command "& {Invoke-WebRequest -Uri %PYTHON_URL% -OutFile %PYTHON_INSTALLER%}"
if exist %PYTHON_INSTALLER% (
    echo Running Python installer...
    start /wait "" %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    echo Python installation complete.
) else (
    echo Failed to download Python installer.
    pause
    exit /b
)

echo Installing MinGW (GCC)...

set "MINGW_URL=https://sourceforge.net/projects/mingw/files/latest/download"
set "MINGW_INSTALLER=mingw-get-setup.exe"

echo Downloading MinGW from %MINGW_URL%...
powershell -Command "& {Invoke-WebRequest -Uri %MINGW_URL% -OutFile %MINGW_INSTALLER%}"
if exist %MINGW_INSTALLER% (
    echo Running MinGW installer...
    start /wait "" %MINGW_INSTALLER%
    echo Please complete the MinGW installation manually through the installer.
    pause
) else (
    echo Failed to download MinGW installer.
    pause
    exit /b
)

setx PATH "%PATH%;C:\MinGW\bin" /M

echo Python and C compiler setup complete.
pause



pip install pystyle
pip install requests
py -m pip install requests
py -m pip install pystyle

cls

echo Installed Modules

pause