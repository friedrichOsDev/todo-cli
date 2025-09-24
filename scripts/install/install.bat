@echo off

cd ../../build

if not exist "./todo.exe" (
    echo Error: todo.exe not found in the build directory.
    echo Please run the build script first.
    pause
    exit /b 1
)

if not exist "C:/Users/%USERNAME%/todo-cli" (
    mkdir "C:/Users/%USERNAME%/todo-cli"
)

copy "./todo.exe" "C:/Users/%USERNAME%/todo-cli/todo.exe" /Y