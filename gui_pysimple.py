import modules.functions as fn
"""
Can be used in tkinter, or designed in PAGE app. 
"""
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo_inbox_key")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")

list_box = sg.Listbox(values=fn.get_todos(), key="todos_listbox_key",
                      enable_events=True, size=(45, 10))

window = sg.Window("My to-do App",
                   layout=[[label],[input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    win_event, win_values = window.read()
    print(1, win_event)
    print(2, win_values)
    print(3, win_values['todos_listbox_key'])
    match win_event:
        case "Add":
            todos = fn.get_todos()
            new_todo = win_values['todo_inbox_key'] + "\n"
            todos.append(new_todo)
            fn.write_todos(todos)
            window['todos_listbox_key'].update(values=todos)
        case "Edit":
            todo_to_edit = win_values['todos_listbox_key'][0]
            new_todo = win_values['todo_inbox_key']
            todos = fn.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'
            fn.write_todos(todos)
            window['todos_listbox_key'].update(values=todos)
        case "todos_listbox_key":
            window['todo_inbox_key'].update(value=win_values['todos_listbox_key'][0])
        case sg.WIN_CLOSED:
            break



window.close()
