import sys

# Command functions

def help():
    print("")
    print("Usage: todo [options]")
    print("Options:")
    print("  add -t <title> -m <message> - Adds a new todo.")
    print("  delete -t <title> - Deletes the specified todo.")
    print("  mark -t <title> - Marks the specified todo as completed.")
    print("  status - Lists all todos and shows their completion status.")
    print("  help - Shows all commands.")
    print("")
    print("Examples:")
    print("  todo add -t \"Buy milk\" -m \"Remember to buy milk after work\"")
    print("  todo mark -t \"Buy milk\"")
    print("  todo delete -t \"Buy milk\"")
    print("  todo status")
    print("  todo help")
    print("")
    print("For more information on this project, visit: https://github.com/friedrichOsDev/todo-cli")
    print("")
    

def add_todo(title, message):
    print(f"Adding a new todo...")
    print(f"Title: {title}")
    print(f"Message: {message}")
    print("Not implemented yet.")
    
def delete_todo(title):
    print(f"Deleting the todo with title: {title}")
    print("Not implemented yet.")
    
def mark_todo(title):
    print(f"Marking the todo with title: {title} as completed")
    print("Not implemented yet.")

def status_todo():
    print("Listing all todos and their completion status")
    print("Not implemented yet.")

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
    
# Main command processing

arguments = sys.argv[1:]

if not arguments:
    help()
    sys.exit(0)
elif arguments[0] == "help":
    help()
    sys.exit(0)
elif arguments[0] == "add":
    if len(arguments) < 5 or arguments[1] != "-t" or arguments[3] != "-m":
        arg_error("add")
    title = arguments[2]
    message = arguments[4]
    add_todo(title, message)
    sys.exit(0)
elif arguments[0] == "delete":
    if len(arguments) < 3 or arguments[1] != "-t":
        arg_error("delete")
    title = arguments[2]
    delete_todo(title)
    sys.exit(0)
elif arguments[0] == "mark":
    if len(arguments) < 3 or arguments[1] != "-t":
        arg_error("mark")
    title = arguments[2]
    mark_todo(title)
    sys.exit(0)
elif arguments[0] == "status":
    if len(arguments) != 1:
        arg_error("status")
    status_todo()
    sys.exit(0)
else:
    unknown_command(arguments[0])