import streamlit as st
import pandas as pd
import mymodule.mycode as mycode
import mymodule.text as text

st.header("🍈プレゼンテーションエリア",anchor='section1',divider='rainbow')
#プログラム
st.code(mycode.code1)
st.write(text.area2)
st.markdown("[go to Top](#section1)")

st.divider()
st.image('images/20240429.png', caption='2024/04/29:為替介入のチャート')

st.markdown("[go to Top](#section1)")
st.divider()

#ビデオ
@st.cache_data
def video():
    st.video('images/penguin_swimming.mp4',loop=True)

st.write('泳ぐペンギン')
video()

st.markdown("[go to Top](#section1)")
st.divider()

#マップ
place=[(35.8712481,139.3243931)]
st.write(f"【ムーミンバレーパーク　{place[0]} の表示】  \nこれはGoogleMapのAPIを使ったほうがよさそうです。")

df = pd.DataFrame(
    data=place,
    columns=['lat', 'lon'])
st.map(df,zoom = 8)

body ="""
#マップ
import streamlit as st
import pandas as pd

place=[(35.8712481,139.3243931)]
st.write(f"【ムーミンバレーパーク{place[0]} の表示】  \\nこれはGoogleMapのAPIを使ったほうがよさそうです。")

df = pd.DataFrame(
    data=place,
    columns=['lat', 'lon'])
st.map(df,zoom = 8)
"""
st.code(body)

st.markdown("[go to Top](#section1)")
st.divider()