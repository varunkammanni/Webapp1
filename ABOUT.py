# pages/ABOUT.py
import streamlit as st


def main():
    st.title("About Us")
    st.markdown("---")

    st.header("Our Story")
    st.write("""
    This is a sample multi-page application built to demonstrate Streamlit's capabilities.
    We're passionate about creating simple yet powerful web applications using Python.
    """)

    # Team section
    st.header("Our Team")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("John Doe")
        st.write("Developer")
        st.write("Expert in Python and Streamlit")

    with col2:
        st.subheader("Jane Smith")
        st.write("Designer")
        st.write("UI/UX Specialist")

    with col3:
        st.subheader("Mike Johnson")
        st.write("Project Manager")
        st.write("Agile Enthusiast")

    # Metrics
    st.markdown("---")
    st.header("Our Stats")
    col1, col2, col3 = st.columns(3)
    col1.metric("Years Experience", "5+")
    col2.metric("Projects Completed", "20+")
    col3.metric("Happy Clients", "15+")


if __name__ == "__main__":
    main()