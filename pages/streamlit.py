import subprocess
from generating_text.comments_data import *
import streamlit as st

# init
if 'generated_text' not in st.session_state:
    st.session_state['generated_text'] = None


# title
st.title('Input your Name below')
myName = st.text_input('Who are you today?')

# generation
if st.button('Generate'):
    st.session_state.generated_text = random_text_generator(myName)

if st.session_state.generated_text:
    st.write(st.session_state.generated_text)

if st.button('Copy'):
    copy_js = """
        <script>
            function copyText() {
                var copyText = document.getElementById("gen_text");
                copyText.select();
                document.execCommand("copy");
            }
        </script>
        <button onclick="copyText()">Copy to Clipboard</button>
    """
    st.markdown(copy_js, unsafe_allow_html=True)



