import streamlit as st

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🔄", layout="centered")

st.header("Mubashir Streamlit Apps")
st.title("🌱 Growth Mindset Challenge")
st.write("Welcome to the Growth Mindset Challenge! This app is designed to help you develop a growth mindset by encouraging you to keep track of your daily growth.")    

name = st.text_input("What is Your Name ?")
if name:
    st.success(f"Great to have you here, {name}! ")

st.title("📝 Simple To-Do List")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

new_task = st.text_input("Enter a new task")

if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.success(f"Task added: {new_task}")
    else:
        st.warning("Please enter a task.")

st.subheader("📋 Your Tasks")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.8, 0.2])
        col1.write(f"{i+1}. {task}")
        if col2.button("❌", key=i):
            st.session_state.tasks.pop(i)
            st.rerun() 
else:
    st.info("No tasks added yet.")

st.write("- - - -")

st.title("🔢 Counter App")

if 'count' not in st.session_state:
    st.session_state.count = 0

st.write(f"Current Count: {st.session_state.count}")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Increment"):
        st.session_state.count += 1
with col2:
    if st.button("Decrement"):
        st.session_state.count -= 1
with col3:
    if st.button("Reset"):
        st.session_state.count = 0

st.write("- - - -")
# st.write("Keep belief that you can always grow and improve. Stay motivated and keep pushing forward!")
# st.write("Created by Mubashir")