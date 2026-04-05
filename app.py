import streamlit as st

st.set_page_config(page_title="AI Homework Notebook")

st.title("📘 AI-Powered Homework & Personalized Notebook")

if "homework" not in st.session_state:
    st.session_state.homework = ""
    st.session_state.deadline = ""
    st.session_state.submitted = False

st.header("👩‍🏫 Teacher Dashboard")

with st.form("teacher_form"):
    subject = st.text_input("Subject")
    topic = st.text_input("Homework Topic")
    deadline = st.text_input("Deadline")
    add = st.form_submit_button("Add Homework")

    if add:
        st.session_state.homework = f"{subject} - {topic}"
        st.session_state.deadline = deadline
        st.session_state.submitted = False
        st.success("Homework added!")

st.header("🧑‍🎓 Student View")

if st.session_state.homework:
    st.write("📌 Homework:", st.session_state.homework)
    st.write("⏰ Deadline:", st.session_state.deadline)

    text = st.text_area("Write your rough answers")

    if st.button("✨ Generate Notes"):
        if text.strip():
            st.subheader("Generated Notes")
            st.write("- " + text.replace(".", "\n- "))
        else:
            st.warning("Write something")

    if st.button("✅ Submit Homework"):
        if text.strip():
            st.session_state.submitted = True
            st.success("Submitted!")
        else:
            st.warning("Cannot submit empty work")

st.header("📊 Status")

if st.session_state.homework:
    if st.session_state.submitted:
        st.success("✅ Completed")
    else:
        st.error("❌ Not Completed")
