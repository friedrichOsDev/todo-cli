# todo-cli

## Introduction

todo-cli is a lightweight and efficient command-line tool for managing your daily tasks directly from the terminal. Designed for programmers and terminal enthusiasts, it helps you organize, track, and complete your todos quickly without leaving your workflow. With simple commands, you can add, mark, delete, and view the status of your tasks, making productivity seamless and distraction-free.

## Features

- **Add a todo**: `todo add -t <title> -m <message>` - Adds a new todo.
- **Delete a todo**: `todo delete -t <title>` - Deletes the specified todo.
- **Mark a todo as done**: `todo mark -t <title>` - Marks the specified todo as completed.
- **View status**: `todo status` - Lists all todos and shows their completion status.
- **Get help**: `todo help` - Shows all commands.

## Installation (Windows only)

1. Clone the repository:
    ```batch
    git clone https://github.com/friedrichOsDev/todo-cli.git
    cd todo-cli
    ```
2. Install dependencies:

    - Install [Python](https://www.python.org/downloads/release/python-3119) version 3.11.9 or higher.
    - You don't need admin rights.

3. Build the project:
    ```batch
    python build.py
    ```
4. Install the program:
    ```batch
    python install.py
    ```
5. Uninstallation:
    ```batch
    python uninstall.py
    ```

## Usage

After installation, run `todo` from your terminal or command prompt.  

**Example commands:**

1. Add a todo: `todo add -t <title> -m <message>`
2. Delete a todo: `todo delete -t <title>`
3. Mark as done: `todo mark -t <title>`
4. View status: `todo status`
5. Get help: `todo help`

**Installation directory:** `C:\Users\<Your Username>\todo-cli`

### Examples (Windows Command Prompt)
```batch
todo status
todo add -t "Buy milk" -m "Remember to buy milk after work"
todo status
todo mark -t "Buy milk"
todo status
todo delete -t "Buy milk"
todo help
```

#### Output (Windows Command Prompt)
![](docs/output.png)

## Contributing

Pull requests are welcome! For major changes, please open an [issue](https://github.com/friedrichOsDev/todo-cli/issues) first to discuss what you would like to change.

## License

This project is licensed under the [MIT License](LICENSE).
