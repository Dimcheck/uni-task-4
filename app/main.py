import streamlit as st
from serializing import convert_mail_object
from io import StringIO

uploaded_file = st.file_uploader(type=['json'], label="Choose a file")
if uploaded_file is not None:

    st.write('filename:', uploaded_file.name)
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    str_data = stringio.read()

    render_data = convert_mail_object(str_data)

    st.write(render_data)
