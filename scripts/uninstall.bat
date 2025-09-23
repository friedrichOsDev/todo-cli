@echo off
echo Do you want to uninstall todo-cli? (Y/N)
set /p userInput=
if /i "%userInput%"=="Y" (
    echo Uninstalling todo-cli...
    rmdir /S /Q "C:/Users/%USERNAME%/todo-cli"
    echo todo-cli has been uninstalled.
) else (
    echo Uninstallation canceled.
)
pause