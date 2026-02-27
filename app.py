import streamlit as st
import base64
import random
import time

# ページの設定
st.set_page_config(page_title="リアル古代魚水槽", layout="wide")

# 背景動画を設定するHTML
def get_base_html(video_path):
    with open(video_path, 'rb') as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    return f"""
        <style>
        #myVideo {{
            position: fixed; right: 0; bottom: 0;
            min-width: 100%; min-height: 100%;
            z-index: -1; object-fit: cover;
        }}
        .stApp {{ background-color: rgba(0,0,0,0); }}
        
        /* 魚群アニメーション */
        @keyframes swim_left {{
            0% {{ transform: translateX(110vw); opacity: 0; }}
            10% {{ opacity: 0.7; }}
            90% {{ opacity: 0.7; }}
            100% {{ transform: translateX(-150vw); opacity: 0; }}
        }}
        .fish {{
            position: fixed; pointer-events: none; z-index: 9999;
            animation: swim_left 4s linear forwards;
        }}
        </style>
        <video autoplay loop muted playsinline id="myVideo">
            <source src="data:video/mp4;base64,{b64}" type="video/mp4">
        </video>
    """

# 背景動画の表示
try:
    st.markdown(get_base_html('ancient_aquarium.mp4'), unsafe_allow_html=True)
except:
    st.error("動画ファイルが見つかりません。")

st.title("🏛️ リアル・デボン紀アクアリウム")

# --- 状態管理の初期化 ---
# ボタンを押した回数を記録するカウンターを作ります
if 'fish_trigger' not in st.session_state:
    st.session_state.fish_trigger = 0

# サイドバー設定
with st.sidebar:
    st.header("水槽管理パネル")
    # ボタンを押すとカウンターを+1する
    if st.button("🐟 魚群"):
        st.session_state.fish_trigger += 1

# カウンターが0より大きい場合（ボタンが押された場合）に魚群を描画
if st.session_state.fish_trigger > 0:
    fish_icons = ["🐟", "🐠", "🐡", "🦈"]
    fishes_html = ""
    
    # 100匹の魚を生成
    # キー（key）をカウンターに連動させることで、毎回「新しい要素」として認識させます
    for i in range(100):
        top = random.randint(0, 95)
        delay = random.uniform(0, 3.0)
        speed = random.uniform(3.0, 5.0)
        size = random.randint(20, 70)
        icon = random.choice(fish_icons)
        fishes_html += f'<div class="fish" style="top:{top}%; animation-delay:{delay}s; animation-duration:{speed}s; font-size:{size}px;">{icon}</div>'
    
    # 一意のID（カウンターを含む）を付与してHTMLを流し込む
    st.markdown(f'<div id="fish-tank-{st.session_state.fish_trigger}">{fishes_html}</div>', unsafe_allow_html=True)
