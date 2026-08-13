import functions
import streamlit as st


todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"].strip()

    if todo:
        todos.append(todo + "\n")
        functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")


# Display todos
completed_todos = []

for index, todo in enumerate(todos):
    todo_text = todo.strip()

    checkbox = st.checkbox(
        todo_text,
        key=f"todo_{index}"
    )

    if checkbox:
        completed_todos.append(index)


# Remove completed todos after the loop
if completed_todos:
    todos = [
        todo for index, todo in enumerate(todos)
        if index not in completed_todos
    ]

    functions.write_todos(todos)
    st.rerun()


st.text_input(
    label="",
    placeholder="Add new todo...",
    on_change=add_todo,
    key="new_todo"
)