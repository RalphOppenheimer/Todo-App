import streamlit as st
import functions as fn

todos = fn.get_todos()

st.title("My Todo App")
st.subheader("This is my todo App")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)
st.radio(options="asd")

st.text_input(label="", placeholder="Add new todo...")

