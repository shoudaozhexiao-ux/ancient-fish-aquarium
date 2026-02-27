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
                transform: translate(-50%, -50%);
                object-fit: cover;
            }}

            /* ボタンのデザイン：画面上部の中央に固定 */
            div.stButton > button {{
                position: fixed;
                top: 30px;        /* 上からの位置 */
                left: 50%;        /* 左から50%の位置へ */
                transform: translateX(-50%); /* 自身の幅の半分だけ左に戻して中央寄せ */
                z-index: 10000;
                background-color: rgba(0, 50, 100, 0.6) !important;
                color: white !important;
                border: 1px solid rgba(255, 255, 255, 0.5) !important;
                backdrop-filter: blur(10px);
                border-radius: 30px !important;
                padding: 10px 30px !important;
                font-weight: bold !important;
                font-size: 18px !important;
                min-width: 200px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            }}
            
            /* 泡（バブル）のアニメーション定義 */
            @keyframes rise {{
                0% {{ bottom: -10%; transform: translateX(0); opacity: 0; }}
                20% {{ opacity: 0.6; }}
                80% {{ opacity: 0.6; }}
                100% {{ bottom: 110%; transform: translateX(20px); opacity: 0; }}
            }}
            .bubble {{
                position: fixed;
                color: rgba(255, 255, 255, 0.4);
                pointer-events: none;
                z-index: 9998;
                animation: rise 5s infinite ease-in;
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

# 2. ボタンを配置（CSSで中央に固定されます）
btn_action = st.button("🐟 魚群 & 泡を呼ぶ")

# 3. ボタンが押された時の演出処理
if btn_action:
    run_id = int(time.time() * 1000)
    
    # 魚群の設定
    fish_icons = ["🐟", "🐠", "🐡", "🦈"]
    fishes_html = ""
    fish_anim = f"swim_{run_id}"
    
    # 泡の設定
    bubbles_html = ""
    
    # 魚群HTML生成
    for i in range(80):
        top = random.randint(0, 95)
        delay = random.uniform(0, 2.5)
        speed = random.uniform(3.0, 5.0)
        size = random.randint(25, 75)
        icon = random.choice(fish_icons)
        fishes_html += f'<div class="fish-{run_id}" style="top:{top}%; animation-delay:{delay}s; animation-duration:{speed}s; font-size:{size}px;">{icon}</div>'
    
    # 泡HTML生成（下から上へ）
    for i in range(30):
        left = random.randint(0, 100)
        delay = random.uniform(0, 3.0)
        size = random.randint(10, 30)
        bubbles_html += f'<div class="bubble" style="left:{left}%; animation-delay:{delay}s; font-size:{size}px;">○</div>'
    
    # 魚群用スタイル
    style_html = f"""
    <style>
    @keyframes {fish_anim} {{
        0% {{ transform: translateX(0); opacity: 0; }}
        5% {{ opacity: 0.8; }}
        95% {{ opacity: 0.8; }}
        100% {{ transform: translateX(-250vw); opacity: 0; }}
    }}
    .fish-{run_id} {{
        position: fixed; left: 110vw; pointer-events: none; z-index: 9999;
        animation: {fish_anim} 4s linear forwards;
    }}
    </style>
    """
    
    st.markdown(style_html + fishes_html + bubbles_html, unsafe_allow_html=True)
