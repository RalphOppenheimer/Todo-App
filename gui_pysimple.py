import modules.functions as fn
"""
Can be used in tkinter, or designed in PAGE app. 
"""
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My to-do App",
                   layout=[[label],[input_box, add_button]],
                   font=('Helvetical', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = fn.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            fn.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close()
