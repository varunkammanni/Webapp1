# pages/CONTACT.py
import streamlit as st


def main():
    st.title("Contact Us")
    st.markdown("---")

    st.header("Get in Touch")
    st.write("We'd love to hear from you!")

    # Contact form
    with st.form(key="contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button(label="Send")

        if submit_button:
            if name and email and message:
                st.success("Thank you for your message! We'll get back to you soon.")
            else:
                st.error("Please fill in all fields.")

    # Contact info
    st.markdown("---")
    st.header("Contact Information")
    st.write("📧 Email: contact@example.com")
    st.write("📞 Phone: (123) 456-7890")
    st.write("🏢 Address: 123 Main St, City, Country")

    # Social media
    st.header("Follow Us")
    col1, col2, col3 = st.columns(3)
    col1.button("Twitter")
    col2.button("LinkedIn")
    col3.button("GitHub")


if __name__ == "__main__":
    main()