import streamlit as st
import mymodule.text as text

st.sidebar.image('images/emp05.png', caption='かわいいペンギン')

st.header("🍇Streamlitのテスト",anchor='section1',divider='rainbow')
st.write(text.area1)
st.divider()
st.markdown("[go to Top](#section1)")
