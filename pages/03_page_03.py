import streamlit as st
import mymodule.text as text

st.header("🎥 Youtubeの動画配信のテスト",anchor='section1', divider='rainbow')

URL = {
"マギアレコード":"""https://www.youtube.com/embed/jI8OMNPbQTA?si=wO37Zc1sHefoyWMG""",
"暁のヨナ":"""https://www.youtube.com/embed/3Tz3vxwJf6I?si=sJGb9PcbHgO5KwS5""",
"ロード・エルメロイⅡ世の事件簿":"""https://www.youtube.com/embed/5loZwcsmn84?si=jjHaLTntPVQ5XK0y""",
"チェンソーマン":"""https://www.youtube.com/embed/dFlDRhvM4L0?si=9tIFZteHGmEobDGP"""
}

option = st.selectbox(
    "🌟テスト動画を選択🌟",
    ("マギアレコード", "暁のヨナ","ロード・エルメロイⅡ世の事件簿","チェンソーマン"))

st.video(URL[option])

st.write("Youtubeの動画を埋め込むには、共有リンクをURLをつかうのではなく埋め込みリンクのURLを使わないと表示されない。この2つはじつは違うのだ。 If you wish to stream youtube on your web_app, you use embedded-link, not share-link.")

st.code("""
URL = \"""youtubeの埋め込みリンク(embedded-link)のURL\"""
st.video(URL)
""")

st.markdown("[go to Top](#section1)")
