import streamlit as st

with st.form(key='profile_form'):
    # テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')

    # セレクトボックス
    age_category = st.radio(
        '年齢層',
        ('子供','大人')
    )

    # ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'ようこそ{name}さん!{address}に爆弾を送りました！')
        st.text(f'あなたは{age_category}です！')