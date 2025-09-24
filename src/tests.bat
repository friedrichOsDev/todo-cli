@echo off
REM Clean up previous test data
if exist todos rmdir /s /q todos
if exist status.json del status.json

REM Test: Add a todo
echo Adding todo "Test1"...
python todo.py add -t Test1 -m "First test todo"

REM Test: Add duplicate todo (should error)
echo Adding duplicate todo "Test1" (should error)...
python todo.py add -t Test1 -m "Duplicate test todo"

REM Test: Mark todo as completed
echo Marking "Test1" as completed...
python todo.py mark -t Test1

REM Test: Status output
echo Checking status...
python todo.py status

REM Test: Delete todo
echo Deleting "Test1"...
python todo.py delete -t Test1

REM Test: Delete non-existent todo (should error)
echo Deleting non-existent todo "Test1" (should error)...
python todo.py delete -t Test1

REM Test: Add multiple todos
echo Adding "Test2" and "Test3"...
python todo.py add -t Test2 -m "Second test todo"
python todo.py add -t Test3 -m "Third test todo"

REM Test: Mark "Test2" as completed
echo Marking "Test2" as completed...
python todo.py mark -t Test2

REM Test: Delete all completed todos
echo Deleting all completed todos...
python todo.py delete -a

REM Test: Status output after deletion
echo Checking status after deletion...
python todo.py status

REM Test: Add with invalid args (should error)
echo Add with invalid args (should error)
python todo.py add

REM Test: Mark with invalid args (should error)
echo Mark with invalid args (should error)
python todo.py mark

REM Test: Delete with invalid args (should error)
echo Delete with invalid args (should error)
python todo.py delete

REM Test: Status with invalid args (should error)
echo Status with invalid args (should error)
python todo.py status invalidArg

REM Test: Help with invalid args (should error)
echo Help with invalid args (should error)
python todo.py help invalidArg

REM Test: todo.py with invalid command (should error)
echo todo.py with invalid command (should error)
python todo.py invalidCommand

echo Tests finished. Please review the output above for correctness.

pause

REM Clean up previous test data
if exist todos rmdir /s /q todos
if exist status.json del status.json
