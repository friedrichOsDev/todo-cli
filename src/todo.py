import sys, os, json

# Command functions

def help():
    print("")
    print("Usage: ")
    print("  todo add -t <title> -m <message> - Adds a new todo.")
    print("  todo delete -t <title> - Deletes the specified todo.")
    print("  todo delete -a - Deletes all completed todos.")
    print("  todo mark -t <title> - Marks the specified todo as completed.")
    print("  todo status - Lists all todos and shows their completion status.")
    print("  todo help - Shows all commands.")
    print("")
    print("Examples:")
    print("  todo add -t \"Buy milk\" -m \"Remember to buy milk after work\"")
    print("  todo mark -t \"Buy milk\"")
    print("  todo delete -t \"Buy milk\"")
    print("  todo delete -a")
    print("  todo status")
    print("  todo help")
    print("")
    print("For more information on this project, visit: https://github.com/friedrichOsDev/todo-cli")
    print("")
    
def add_todo(title, message):
    todos = load_todos()
    
    if f"{title}.todo" in todos:
        print("")
        print(f"Error: A todo with the title '{title}' already exists.")
        print("")
        sys.exit(1)
    else:
        path = os.path.join("todos", f"{title}.todo")
        
        with open(path, "w") as f:
            f.write(message)
        
        set_status_of_todo(title, False)
    
def delete_todo(title):
    todos = load_todos()
    
    if f"{title}.todo" not in todos:
        print("")
        print(f"Error: No todo found with the title '{title}'.")
        print("")
        sys.exit(1)
    else:
        path = os.path.join("todos", f"{title}.todo")
        os.remove(path)
        set_status_of_todo(title, None)

def delete_todos_completed():
    todos = load_todos()
    
    if os.path.exists("status.json"):
        with open("status.json", "r") as f:
            status_data = json.load(f)
    else:
        status_data = {}
    
    for filename, _ in todos.items():
        title = filename[:-5]
        if status_data.get(title, False):
            delete_todo(title)
    
def mark_todo(title):
    todos = load_todos()
    
    if f"{title}.todo" not in todos:
        print("")
        print(f"Error: No todo found with the title '{title}'.")
        print("")
        sys.exit(1)
    else:
        set_status_of_todo(title, True)

def status_todo():
    todos = load_todos()
    
    status_path = "status.json"
    if os.path.exists(status_path):
        with open(status_path, "r") as f:
            status_data = json.load(f)
    else:
        status_data = {}
    
    print("")
    print("Todo List Status:")
    if not todos:
        print("No todos found.")
        print("")
    else:
        for filename, message in todos.items():
            title = filename[:-5]  # Remove .todo extension
            completed = status_data.get(title, False)
            status_str = "Completed" if completed else "Not Completed"
            print(f"- Title: {title}")
            print(f"  Message: {message}")
            print(f"  Status: {status_str}")
            print("")
    
# Error handling functions
  
def arg_error(command):
    print("")
    print(f"Error: Invalid arguments for '{command}' command.")
    help()
    sys.exit(1)
    
def unknown_command(command):
    print("")
    print(f"Error: Unknown command '{command}'.")
    help()
    sys.exit(1)
    
# Todo storage functions

def load_todos():
    todos = {}
    
    if not os.path.exists("todos"):
        os.makedirs("todos")
        
    for filename in os.listdir("todos"):
        if filename.endswith(".todo"):
            with open(os.path.join("todos", filename), "r") as f:
                todos[filename] = str(f.read())
                
    return todos

def set_status_of_todo(title, completed): # completed: True | False | None
    status_path = "status.json"
    
    if os.path.exists(status_path):
        with open(status_path, "r") as f:
            status_data = json.load(f)
    else:
        status_data = {}
    if completed == None:
        del status_data[title] # None
    else:
        status_data[title] = completed  # True | False
    
    with open(status_path, "w") as f:
        json.dump(status_data, f, indent=4)

# Initialization  

def init():
    if not os.path.exists("todos"):
        os.makedirs("todos")
        
    if not os.path.exists("status.json"):
        with open("status.json", "w") as f:
            json.dump({}, f)
            
    return sys.argv[1:]
    
arguments = init()

# Main command processing

if not arguments or (arguments[0] == "help" and len(arguments) == 1):
    help()
    sys.exit(0)

cmd = arguments[0]

if cmd == "add":
    if len(arguments) == 5 and arguments[1] == "-t" and arguments[3] == "-m":
        add_todo(arguments[2], arguments[4])
        sys.exit(0)
    else:
        arg_error("add")

elif cmd == "delete":
    if len(arguments) == 3 and arguments[1] == "-t":
        delete_todo(arguments[2])
    elif len(arguments) == 2 and arguments[1] == "-a":
        delete_todos_completed()
    else:
        arg_error("delete")

elif cmd == "mark":
    if len(arguments) == 3 and arguments[1] == "-t":
        mark_todo(arguments[2])
        sys.exit(0)
    else:
        arg_error("mark")

elif cmd == "status":
    if len(arguments) == 1:
        status_todo()
        sys.exit(0)
    else:
        arg_error("status")

else:
    unknown_command(cmd)