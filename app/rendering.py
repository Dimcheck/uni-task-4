import streamlit as st
from serializing import convert_mail_object


class RenderData:
    def __init__(self, str_data) -> None:
        self.render_data = convert_mail_object(str_data)
        self.columns = self.render_data.columns.to_list()

        self.date = self.columns[2]
        self.by = self.columns[4]
        self.name = self.columns[1]

    def render_table(self):
        return st.write(self.render_data)

    def render_chart(self):
        selected_info = self.render_data[[
            self.date,
            self.name,
            self.by
        ]]
        grouped_data = selected_info.groupby(self.date).size()
        st.header(f'Line Chart based on "{self.date}"')
        return st.line_chart(grouped_data)

