import streamlit as st
import functions

print('Starting App')
todos = functions.get_todo()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todo(todos)


print("After addtodo function")

st.title('My To-do App')
st.subheader("Welcome and try our To-do's app")
st.write('We can add, edit, track todos or complete item in our list with this easy app')

for todo in todos:
    st.checkbox(todo)

st.text_input(label='todo:', placeholder='Add a new to-do', key='new_todo', on_change=add_todo)
st.session_state

print('closing app')
