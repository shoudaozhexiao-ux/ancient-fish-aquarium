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
            .main .block-container {{ padding: 0; max-width: 100%; }}
            .stApp {{ background-color: rgba(0,0,0,0); }}
            
            #myVideo {{
                position: fixed; top: 50%; left: 50%;
                min-width: 100%; min-height: 100%;
                width: auto; height: auto;
                z-index: -2;
                transform: translate(-50%, -50%);
                object-fit: cover;
            }}

            /* ボタンのデザイン：画面中央上部に固定 */
            div.stButton > button {{
                position: fixed;
                top: 30px;
                left: 50%;
                transform: translateX(-50%);
                z-index: 10000;
                background-color: rgba(0, 50, 100, 0.6) !important;
                color: white !important;
                border: 1px solid rgba(255, 255, 255, 0.5) !important;
                backdrop-filter: blur(10px);
                border-radius: 30px !important;
                padding: 10px 30px !important;
                font-weight: bold !important;
                font-size: 18px !important;
                min-width: 180px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            }}
            
            /* 泡（バブル）のアニメーション：初期位置を完全に画面外(120%)に */
            @keyframes rise {{
                0% {{ bottom: -20%; transform: translateX(0); opacity: 0; }}
                20% {{ opacity: 0.6; }}
                80% {{ opacity: 0.6; }}
                100% {{ bottom: 120%; transform: translateX(30px); opacity: 0; }}
            }}
            .bubble {{
                position: fixed;
                color: rgba(255, 255, 255, 0.4);
                pointer-events: none;
                z-index: 9998;
                /* 初回に変な場所に表示されないよう初期状態を隠す */
                bottom: -20%; 
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

# 2. ボタンを配置（テキストを短縮）
btn_action = st.button("🐟 魚群 & 泡")

# 3. ボタンが押された時の演出処理
if btn_action:
    # 実行のたびにユニークなIDを作成してアニメーションをリセット
    run_id = int(time.time() * 1000)
    
    # 演出用のHTMLを生成
    fishes_html = ""
    bubbles_html = ""
    fish_anim_name = f"swim_{run_id}"
    bubble_anim_name = f"rise_{run_id}"
    
    # 魚群の設定
    fish_icons = ["🐟", "🐠", "🐡", "🦈"]
    for i in range(80):
        top = random.randint(0, 95)
        delay = random.uniform(0, 2.0)
        speed = random.uniform(3.0, 5.0)
        size = random.randint(25, 75)
        icon = random.choice(fish_icons)
        fishes_html += f'<div class="fish-{run_id}" style="top:{top}%; animation-delay:{delay}s; animation-duration:{speed}s; font-size:{size}px;">{icon}</div>'
    
    # 泡の設定（個別のアニメーションを付与）
    for i in range(40):
        left = random.randint(0, 100)
        delay = random.uniform(0, 2.5)
        duration = random.uniform(4.0, 6.0)
        size = random.randint(10, 35)
        bubbles_html += f'<div class="bubble" style="left:{left}%; animation: {bubble_anim_name} {duration}s ease-in {delay}s forwards; font-size:{size}px;">○</div>'
    
    # この実行専用のCSSアニメーション
    style_html = f"""
    <style>
    @keyframes {fish_anim_name} {{
        0% {{ transform: translateX(0); opacity: 0; }}
        5% {{ opacity: 0.8; }}
        95% {{ opacity: 0.8; }}
        100% {{ transform: translateX(-250vw); opacity: 0; }}
    }}
    @keyframes {bubble_anim_name} {{
        0% {{ bottom: -10%; transform: translateX(0); opacity: 0; }}
        15% {{ opacity: 0.6; }}
        85% {{ opacity: 0.6; }}
        100% {{ bottom: 110%; transform: translateX(20px); opacity: 0; }}
    }}
    .fish-{run_id} {{
        position: fixed; left: 110vw; pointer-events: none; z-index: 9999;
        animation: {fish_anim_name} 4s linear forwards;
    }}
    </style>
    """
    
    st.markdown(style_html + fishes_html + bubbles_html, unsafe_allow_html=True)
