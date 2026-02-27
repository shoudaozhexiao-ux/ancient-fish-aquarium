import streamlit as st
import base64
import random
import time

# ページの設定
st.set_page_config(page_title="リアル古代魚水槽", layout="wide")

# --- 背景動画を「全体中央表示」に固定するための関数 ---
def display_background_video(video_path):
    try:
        with open(video_path, 'rb') as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        st.markdown(f"""
            <style>
            /* Streamlit全体の余白をゼロにする */
            .main .block-container {{
                padding: 0;
                max-width: 100%;
            }}
            .stApp {{ background-color: rgba(0,0,0,0); }}
            
            #myVideo {{
                position: fixed;
                top: 50%;
                left: 50%;
                min-width: 100%; 
                min-height: 100%;
                width: auto;
                height: auto;
                z-index: -2;
                /* 中央寄せの決定版：真ん中にずらして配置 */
                transform: translate(-50%, -50%);
                /* 隙間なく埋める設定 */
                object-fit: cover;
            }}

            /* ボタンのデザイン（右上固定） */
            .stButton > button {{
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 10000;
                background-color: rgba(0, 50, 100, 0.4) !important;
                color: white !important;
                border: 1px solid rgba(255, 255, 255, 0.5) !important;
                backdrop-filter: blur(8px);
                border-radius: 30px !important;
                padding: 12px 24px !important;
                font-weight: bold !important;
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

# 2. ボタンを配置
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
