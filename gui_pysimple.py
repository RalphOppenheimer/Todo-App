import modules.functions as fn
"""
Can be used in tkinter, or designed in PAGE app. 
"""
import PySimpleGUI as sg
import time

sg.theme("Default1")

clock = sg.Text('', key='clock_key')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo_inbox_key")
#add_button = sg.Button("Add")
add_button = sg.Button(image_source=r'files/images/add.png', mouseover_colors="LightBlue2",
                       tooltip='Add Todo')
edit_button = sg.Button("Edit")
#complete_button = sg.Button("Complete")
complete_button = sg.Button(image_source=r'files/images/complete.png')
exit_button = sg.Button("Exit")

list_box = sg.Listbox(values=fn.get_todos(), key="todos_listbox_key",
                      enable_events=True, size=(45, 10))

window = sg.Window("My to-do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button]],
                   font=('Helvetica', 20))

while True:
    win_event, win_values = window.read(timeout=10)
    window['clock_key'].update(value=time.strftime(" %A %Y%m%d-%H%M%S"))
    match win_event:
        case "Add":
            todos = fn.get_todos()
            new_todo = win_values['todo_inbox_key'] + "\n"
            todos.append(new_todo)
            fn.write_todos(todos)
            window['todos_listbox_key'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = win_values['todos_listbox_key'][0]
                new_todo = win_values['todo_inbox_key']
                todos = fn.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                fn.write_todos(todos)
                window['todos_listbox_key'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=('Helvetica', 20))
        case "Complete":
            try:
                todo_to_complete = win_values['todos_listbox_key'][0]
                todos = fn.get_todos()
                todos.remove(todo_to_complete)
                # index = todos.index(todo_to_complete)
                # todos.pop(index)
                fn.write_todos(todos)
                window['todos_listbox_key'].update(values=todos)
                window['todo_inbox_key'].update(value="")
            except IndexError:
                sg.popup("Please select an item first")
        case "Exit":
            break
        case "todos_listbox_key":
            window['todo_inbox_key'].update(value=win_values['todos_listbox_key'][0])
        case sg.WIN_CLOSED:
            break



window.close()
