import streamlit as st
from io import StringIO
from rendering import RenderData


uploaded_file = st.file_uploader(type=['json'], label="Choose a file")
if uploaded_file is not None:

    st.write('Перелік місцевих цільових програм у тому числі посилання на оприлюднені ресурси в мережі інтернет')
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    str_data = stringio.read()

    page_data = RenderData(str_data)

    page_data.render_table()
    page_data.render_chart()
