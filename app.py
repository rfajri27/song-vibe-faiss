import streamlit as st
from modules.inference import suggest


def run():

    # Set page configuration to wide and hide the menu
    st.set_page_config(layout="centered")

    # Background image CSS
    background_style = """
    <style>
        body {
            background-image: url('https://example.com/your-image-url.jpg');
            background-size: cover;
        }
    </style>
    """

    # Display the background style
    st.markdown(background_style, unsafe_allow_html=True)

    # Text input in the center of the page
    st.markdown(
        "<h1 style='text-align: center; color: white;'>SoundSoul: Find Songs That Match Your Mood</h1>",
        unsafe_allow_html=True,
    )
    user_input = st.text_input(
        "Describe your mood in the text box below, and we will do the rest. "
    )

    # You can do something with the user input here
    if user_input:
        st.write(suggest(user_input))
    else:
        st.write("")


if __name__ == "__main__":
    run()
