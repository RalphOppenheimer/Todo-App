import streamlit as st
import functions as fn

todos = fn.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + '\n'
    print(new_todo)
    todos.append(new_todo)
    fn.write_todos(todos)



st.title("My Todo App")
st.subheader("This is my todo App")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Entry", placeholder="Add new todo...", on_change=add_todo, key="new_todo")

