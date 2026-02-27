import streamlit as st
import base64
import random
import time

# ページの設定
st.set_page_config(page_title="リアル古代魚水槽", layout="wide")

# 背景動画を設定するHTML
def display_background_video(video_path):
    try:
        with open(video_path, 'rb') as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <style>
            .stApp {{ background-color: rgba(0,0,0,0); }}
            #myVideo {{
                position: fixed; right: 0; bottom: 0;
                min-width: 100%; min-height: 100%;
                z-index: -2; object-fit: cover;
            }}
            /* メイン画面のボタンを右上に固定するスタイル */
            .stButton > button {{
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 10000;
                background-color: rgba(255, 255, 255, 0.2) !important;
                color: white !important;
                border: 1px solid rgba(255, 255, 255, 0.5) !important;
                backdrop-filter: blur(5px);
                border-radius: 20px !important;
                padding: 10px 20px !important;
                transition: all 0.3s;
            }}
            .stButton > button:hover {{
                background-color: rgba(255, 255, 255, 0.4) !important;
                border: 1px solid white !important;
                transform: scale(1.05);
            }}
            </style>
            <video autoplay loop muted playsinline id="myVideo">
                <source src="data:video/mp4;base64,{b64}" type="video/mp4">
            </video>
        """, unsafe_allow_html=True)
    except:
        st.error("動画ファイルが見つかりません。")

# 1. 動画を表示
display_background_video('ancient_aquarium.mp4')

# 2. メイン画面にボタンを配置（サイドバーから出しました）
# ※ st.title の下などに置くと、スクロールしても右上に固定されます
btn_fish = st.button("🐟 魚群を呼ぶ")

# 3. 魚群ボタンが押された時の処理
if btn_fish:
    fish_icons = ["🐟", "🐠", "🐡", "🦈"]
    fishes_html = ""
    run_id = int(time.time() * 1000)
    animation_name = f"swim_left_{run_id}"
    
    style_html = f"""
    <style>
    @keyframes {animation_name} {{
        0% {{ transform: translateX(0); opacity: 0; }}
        5% {{ opacity: 0.8; }}
        95% {{ opacity: 0.8; }}
        100% {{ transform: translateX(-250vw); opacity: 0; }}
    }}
    .fish-{run_id} {{
        position: fixed; left: 110vw; pointer-events: none; z-index: 9999;
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
    
    st.markdown(style_html + fishes_html, unsafe_allow_html=True)
