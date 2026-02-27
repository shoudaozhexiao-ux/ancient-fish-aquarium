import streamlit as st
import base64
import time
import random

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
            from {{ transform: translateX(105vw); }}
            to {{ transform: translateX(-100vw); }}
        }}
        .fish-group-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 999;
            overflow: hidden;
        }}
        .fish-individual {{
            position: absolute;
            font-size: 30px;
            opacity: 0.7;
            animation: swim_left 3s linear forwards;
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
    st.error("動画が見つかりません。GitHubのファイル名を確認してください。")

# --- 魚群の制御ロジック ---
if 'show_school' not in st.session_state:
    st.session_state.show_school = False

with st.sidebar:
    st.header("水槽管理パネル")
    # ボタン名を「魚群」に変更
    if st.button("🐟 魚群"):
        st.session_state.show_school = True

# 魚群ボタンが押された時の処理
if st.session_state.show_school:
    # 大量の魚を生成（ランダムな高さと遅延）
    fishes_html = ""
    fish_icons = ["🐟", "🐠", "🐡", "🦈"] # 古代魚に見立てたバリエーション
    
    for i in range(50): # 魚の数を50匹に増量
        top = random.randint(5, 90)     # 出現する高さ（％）
        delay = random.uniform(0, 1.5)  # 出現のタイミングをずらす
        size = random.randint(20, 50)   # 魚のサイズに変化をつける
        speed = random.uniform(2.5, 4.0) # 泳ぐスピードに変化をつける
        icon = random.choice(fish_icons)
        
        fishes_html += f"""
        <div class="fish-individual" style="
            top: {top}%; 
            animation-delay: {delay}s; 
            animation-duration: {speed}s;
            font-size: {size}px;
        ">{icon}</div>
        """
    
    full_school_html = f'<div class="fish-group-container">{fishes_html}</div>'
    st.markdown(full_school_html, unsafe_allow_html=True)
    
    # 状態のリセット
    time.sleep(0.1)
    st.session_state.show_school = False
