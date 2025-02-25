# APP.py (main file)
import streamlit as st

# Set page config (must be first Streamlit command)
st.set_page_config(
    page_title="Multi-Page App",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)


def main():
    # Sidebar navigation
    st.sidebar.title("Navigation")
    st.sidebar.markdown("---")

    # Custom styling
    st.sidebar.markdown("""
        <style>
        .sidebar .sidebar-content {
            background-color: #f0f2f6;
        }
        </style>
    """, unsafe_allow_html=True)

    # Main page content
    st.title("Welcome to Multi-Page App")
    st.markdown("---")

    # Introduction
    st.header("Home Page")
    st.write("""
    This is a multi-page web application built with Streamlit.
    Use the sidebar to navigate between different pages.
    """)

    # Example features
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Features")
        st.write("- Multiple pages")
        st.write("- Responsive design")
        st.write("- Interactive elements")

    with col2:
        st.subheader("Tech Stack")
        st.write("- Python")
        st.write("- Streamlit")
        st.write("- Custom CSS")

    # Example interactive element
    st.markdown("---")
    st.subheader("Try It Out")
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Hello, {name}! Welcome to the app!")


if __name__ == "__main__":
    main()