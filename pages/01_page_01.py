import streamlit as st
import mymodule.souba as souba

st.header("💰外貨の収支レポート",anchor='section1',divider='rainbow')
st.write(souba.page01)
st.write(souba.comment)
st.divider()
st.markdown("[go to Top](#section1)")
