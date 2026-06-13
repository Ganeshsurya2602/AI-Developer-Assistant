import streamlit as st 
from router import router_task

st.title("AI Developer Assistant")
prompt = st.text_area("Ask coding question")
if st.button("Run AI Assistant"):
    if prompt.strip():
        response = router_task(prompt)

        st.markdown("### AI Response")
        st.code(response, language="python")
    else:
        st.warning("Please enter a prompt")
