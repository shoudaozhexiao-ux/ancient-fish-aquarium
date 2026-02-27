import streamlit as st
import base64
import random

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
    st.error("動画ファイル 'ancient_aquarium.mp4' が見つかりません。")

st.title("🏛️ リアル・デボン紀アクアリウム")

# サイドバー設定
with st.sidebar:
    st.header("水槽管理パネル")
    # ボタンが押されたことを判定
    btn_fish = st.button("🐟 魚群")

# 魚群ボタンが押された時の処理
if btn_fish:
    fish_icons = ["🐟", "🐠", "🐡", "🦈"]
    fishes_html = ""
    # 100匹に増やして「埋め尽くす」感を強化
    for i in range(100):
        top = random.randint(0, 95)
        delay = random.uniform(0, 3.0)  # 3秒かけて次々と現れる
        speed = random.uniform(3.0, 5.0) # 泳ぐ速さに個体差
        size = random.randint(20, 70)   # 大きさに個体差
        icon = random.choice(fish_icons)
        
        fishes_html += f'<div class="fish" style="top:{top}%; animation-delay:{delay}s; animation-duration:{speed}s; font-size:{size}px;">{icon}</div>'
    
    # st.markdownを使って直接ボディに流し込む（コンポーネントを使わない方法に変更）
    st.markdown(f'<div id="fish-tank">{fishes_html}</div>', unsafe_allow_html=True)
