def get_todos(filepath):
    with open(filepath, 'r') as file:
        my_todos = file.readline()
    return my_todos


def write_todos(filepath, new_task):
    with open(filepath, "w") as file:
        file.writelines(new_task)


while True:
    user_action = input('Type add, show, edit, complete or exit: ')

    user_action = user_action.strip()
    if user_action.startswith("add"):
        # Read user's actions starting at index 4
        todo = user_action[4:]
        todos = get_todos('todos.txt')
        todos.join('\n' + todo + '\n')
        write_todos("todos.txt", todos)

    elif user_action.startswith("show"):
        # Read user's actions starting at index 5
        todo = user_action[5:]
        todos = get_todos('todos.txt')
        for line in todos:
            # Print the line
            print(line, end='')

    elif user_action.startswith('edit'):
        try:
            # Read user's actions starting at index 4
            number = int(user_action[5:])
            print(number)
            number -= 1
            todos = get_todos("todos.txt")
            new_todo = input("Enter new todo:")
            write_todos("todos.txt", new_todo)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('show'):
        todos = get_todos("todos.txt")
        for index, item in todos:
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("Exit"):
        exit(0)




