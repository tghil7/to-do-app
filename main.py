def get_todos(filepath):
    with open(filepath, 'r') as file:
        my_todos = file.readlines()
    return my_todos


def append_todos(filepath, new_task):
    with open(filepath, "a") as file:
        file.write('\n')
        file.writelines(new_task)


def write_todos(filepath, this_todo):
    with open("todos.txt", "w") as file:
        file.write('\n')
        file.writelines(this_todo)


while True:
    user_action = input('Type add, show, edit, delete or exit: ')

    user_action = user_action.strip()
    if user_action.startswith("add"):
        # Read user's actions starting at index 4
        todo = [user_action[4:]]
        append_todos('todos.txt', todo)

    elif user_action.startswith("show"):
        # Read user's actions starting at index 5
        todo = user_action[5:]
        todos = get_todos('todos.txt')
        for line in todos:
            # Print the line
            print(line, end='')
        print('\n')

    elif user_action.startswith('delete'):
        try:
            # Read user's actions starting at index 4
            number = int(user_action[7])
            print(number)
            todos = get_todos("todos.txt")
            print('Item to remove:{0}'.format(todos[number]))
            todos.remove(todos[number])
            # Need to find a way to change the size of an array
            write_todos("todos.txt", todos)
            print('\n Length of the list:{0}'.format(len(todos)))
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('edit'):
        try:
            # Read user's actions starting at index 4
            number = int(user_action[5:])
            print(number)
            todos = get_todos("todos.txt")
            new_todo = input("Enter new todo:")
            print('Item to remove:{0}'.format(todos[number]))
            todos.remove(todos[number])
            todos.insert(number, new_todo)
            write_todos("todos.txt", todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('show'):
        todos = get_todos("todos.txt")
        for index, item in todos:
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("exit"):
        exit(0)
