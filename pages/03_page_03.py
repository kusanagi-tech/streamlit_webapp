import streamlit as st
import mymodule.text as text

st.header("🎥 Youtubeの動画配信のテスト",anchor='section1', divider='rainbow')

URL = {
"魔法少女まどか☆マギカ":"""https://www.youtube.com/embed/ks8WPvlQpbg?si=RWDi-msE8z-aXx4j""",
"暁のヨナ":"""https://www.youtube.com/embed/3Tz3vxwJf6I?si=sJGb9PcbHgO5KwS5""",
"デビルマンレディー 第1話":"""https://www.youtube.com/embed/jQipkErPU6Q?si=IhaKBROmFP2IiRMB""",
"チェンソーマン":"""https://www.youtube.com/embed/dFlDRhvM4L0?si=9tIFZteHGmEobDGP"""
}

select = list(URL.keys())

option = st.selectbox("🌟テスト動画を選択🌟",(select[0], select[1],select[2],select[3]))

st.video(URL[option])

st.write("Youtubeの動画を埋め込むには、共有リンクをURLをつかうのではなく埋め込みリンクのURLを使わないと表示されない。この2つはじつは違うのだ。 If you wish to stream youtube on your web_app, you use embedded-link, not share-link.")

st.code("""
URL = \"""youtubeの埋め込みリンク(embedded-link)のURL\"""
st.video(URL)
""")

st.markdown("[go to Top](#section1)")
