def get_todos(filepath):
    with open(filepath, 'r') as file:
        my_todos = file.readline()
    return my_todos


def add_todos(todo):
    todos.append(todo + '\n')
    with open('todos.txt', "w") as file:
        file.writelines(todos)


while True:
    user_action = input('Type add, show, edit, complete or exit')
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos('todos.txt')

        todos = get_todos()
