@echo off

cd ../../

if exist "build" (
    rmdir /s /q "build"
)

mkdir "build"
pyinstaller --onefile --distpath "build" --workpath "build/build_temp" --specpath "build" "./src/todo.py"