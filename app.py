import streamlit as st
import base64
import random
import time

# ページの設定
st.set_page_config(page_title="リアル古代魚水槽", layout="wide")

# 背景動画を設定するHTML
def get_base_html(video_path):
    try:
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
            </style>
            <video autoplay loop muted playsinline id="myVideo">
                <source src="data:video/mp4;base64,{{b64}}" type="video/mp4">
            </video>
        """.replace("{{b64}}", b64)
    except:
        return ""

# 背景動画の表示
base_html = get_base_html('ancient_aquarium.mp4')
if base_html:
    st.markdown(base_html, unsafe_allow_html=True)

st.title("🏛️ リアル・デボン紀アクアリウム")

# サイドバー設定
with st.sidebar:
    st.header("水槽管理パネル")
    # ボタンが押されたらTrueを返す
    btn_fish = st.button("🐟 魚群")

# 魚群ボタンが押された時の処理
if btn_fish:
    fish_icons = ["🐟", "🐠", "🐡", "🦈"]
    fishes_html = ""
    # 実行のたびにユニークなID（タイムスタンプ）を作成
    run_id = int(time.time() * 1000)
    
    # この実行専用のアニメーションを定義（名前を変えることで強制的に再発動させる）
    animation_name = f"swim_left_{run_id}"
    
    # 魚群のスタイル定義
    style_html = f"""
    <style>
    @keyframes {animation_name} {{
        0% {{ transform: translateX(0); opacity: 0; }}
        5% {{ opacity: 0.8; }}
        95% {{ opacity: 0.8; }}
        100% {{ transform: translateX(-250vw); opacity: 0; }}
    }}
    .fish-{run_id} {{
        position: fixed; 
        left: 110vw; 
        pointer-events: none; 
        z-index: 9999;
        animation: {animation_name} 4s linear forwards;
    }}
    </style>
    """
    
    for i in range(100):
        top = random.randint(0, 95)
        delay = random.uniform(0, 2.0)
        speed = random.uniform(3.0, 5.0)
        size = random.randint(25, 75)
        icon = random.choice(fish_icons)
        fishes_html += f'<div class="fish-{run_id}" style="top:{top}%; animation-delay:{delay}s; animation-duration:{speed}s; font-size:{size}px;">{icon}</div>'
    
    # スタイルと魚群をまとめて表示
    st.markdown(style_html + fishes_html, unsafe_allow_html=True)
