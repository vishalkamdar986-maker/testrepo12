import streamlit as st

st.set_page_config(
    page_title="Login Page",
    page_icon="🔐",
    layout="centered"
)

# Demo credentials
USERNAME = "admin"
PASSWORD = "admin123"

st.title("🔐 Login Page")
st.write("Please log in to continue.")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login", use_container_width=True):
    if username == USERNAME and password == PASSWORD:
        st.session_state["logged_in"] = True
        st.success("Login successful!")

    else:
        st.error("Invalid username or password.")

if st.session_state.get("logged_in", False):
    st.subheader("Welcome to the Dashboard!")
    st.write("You are successfully logged in.")
    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()