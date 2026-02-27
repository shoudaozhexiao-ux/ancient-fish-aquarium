import streamlit as st
import base64
import time

# ページの設定
st.set_page_config(page_title="リアル古代魚水槽", layout="wide")

# 動画背景を設定するHTML
def get_video_html(video_path):
    with open(video_path, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    return f"""
        <style>
        #myVideo {{
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%; 
            min-height: 100%;
            z-index: -1;
            object-fit: cover;
        }}
        .stApp {{
            background-color: rgba(0,0,0,0);
        }}
        /* 魚群のアニメーション設定 */
        @keyframes swim_left {{
            from {{ transform: translateX(100vw); }}
            to {{ transform: translateX(-100vw); }}
        }}
        .fish-group {{
            position: fixed;
            top: 40%;
            left: 0;
            width: 100%;
            height: 200px;
            pointer-events: none;
            z-index: 10;
            display: flex;
            gap: 50px;
            animation: swim_left 4s linear forwards;
        }}
        .fish-icon {{
            font-size: 40px;
            opacity: 0.6;
            filter: grayscale(0.5);
        }}
        </style>
        <video autoplay loop muted playsinline id="myVideo">
            <source src="data:video/mp4;base64,{b64}" type="video/mp4">
        </video>
    """

# タイトル
st.title("🏛️ リアル・デボン紀アクアリウム")

# 動画背景の読み込み
try:
    st.markdown(get_video_html('ancient_aquarium.mp4'), unsafe_allow_html=True)
except:
    st.error("動画が見つかりません。")

# --- 魚群の制御ロジック ---
if 'show_school' not in st.session_state:
    st.session_state.show_school = False

with st.sidebar:
    st.header("水槽管理パネル")
    # 「魚群」ボタンに変更
    if st.button("🐟 魚群を表示"):
        st.session_state.show_school = True

# 魚群ボタンが押された時の処理
if st.session_state.show_school:
    # 魚群をHTML/CSSアニメーションで表示
    # 魚のアイコン（🐟）を並べて右から左へ流す
    school_html = f"""
    <div class="fish-group">
        <div class="fish-icon">🐟</div>
        <div class="fish-icon" style="margin-top:40px;">🐟</div>
        <div class="fish-icon" style="margin-top:-30px;">🐟</div>
        <div class="fish-icon">🐟</div>
        <div class="fish-icon" style="margin-top:20px;">🐟</div>
        <div class="fish-icon">🐟</div>
    </div>
    """
    st.markdown(school_html, unsafe_allow_html=True)
    
    # アニメーションが終わる頃にフラグをリセット
    time.sleep(0.1) # 表示を安定させるための微調整
    st.session_state.show_school = False
