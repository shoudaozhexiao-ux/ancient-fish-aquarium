import streamlit as st
import base64

# ページの設定（タイトルなど）
st.set_page_config(page_title="リアル古代魚水槽", layout="wide")

# 動画ファイルを読み込んでWebで表示できる形式に変換する関数
def get_video_html(video_path):
    with open(video_path, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    return f"""
        <style>
        /* 背景動画を全画面に固定する設定 */
        #myVideo {{
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%; 
            min-height: 100%;
            z-index: -1;
            object-fit: cover;
        }}
        /* Streamlitの元の背景を透明にする */
        .stApp {{
            background-color: rgba(0,0,0,0);
        }}
        </style>
        <video autoplay loop muted playsinline id="myVideo">
            <source src="data:video/mp4;base64,{b64}" type="video/mp4">
        </video>
    """

# タイトル表示
st.title("🏛️ リアル・デボン紀アクアリウム")

# 動画の表示実行
try:
    video_html = get_video_html('ancient_aquarium.mp4')
    st.markdown(video_html, unsafe_allow_html=True)
    st.write("3億8千万年前の海が、最高画質で蘇りました。")
except Exception as e:
    st.error(f"動画の読み込みに失敗しました。ファイル名を確認してください。: {e}")

# サイドバーに操作パネルを作成
with st.sidebar:
    st.header("水槽管理パネル")
    st.info("デボン紀：ダンクルオステウスの時代を表示中")
    if st.button("エサをあげる"):
        st.balloons()
        st.success("エサを投げ入れました！")
