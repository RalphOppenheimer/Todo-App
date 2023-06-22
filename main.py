# import modules.functions as fn
from modules.functions import write_todos, get_todos
# from modules import functions
import time
prompt = "Type add or show:"
index = 0
now = time.strftime(" %A %Y%m%d-%H%M%S")

if __name__ == '__main__':
    print("Time below")
    print(f"It is{now}")
    while True:
        user_action = input("Type add, show, edit or exit: ")
        user_action = user_action.strip()  # Removing white chars from the input.
        if user_action.startswith('add'):
            todo = user_action[4:]
            todos = get_todos()
            todos.append(todo + '\n')
            write_todos(todos)
            # file.write() for string write

        elif user_action.startswith('show'):
            todos = get_todos()
            # List comprehensions (better choice):
            # new_todos = [item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                item = item.strip('\n')
                number = index + 1
                print(rf"{number}.{item}")

        elif user_action.startswith('edit'):
            try:
                number = int(user_action[5:])
                index = number - 1
                todos = get_todos()
                existing_todo = todos[index]
                new_todo = input("Enter new Todo: ")
                todos[index] = new_todo + '\n'
                write_todos(todos)
            except ValueError:
                print("Enter a number of Todo. ")
                continue

        elif user_action.startswith('exit'):
            break

        elif user_action.startswith('complete'):
            try:
                number = int(user_action[9:])
                todos = get_todos()
                index = number - 1
                todo_to_remove = todos[index]
                todos.pop(index)
                write_todos(todos)
                message = f"Todo {todo_to_remove} was removed from the list"
                print(message)
            except IndexError:
                print("Item of given number not found.")
            except ValueError:
                print("Enter a number of Todo.")
        else:
            print("Unknown choice. Try Again.")
