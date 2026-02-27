import streamlit as st
import base64
import random
import time

# ページの設定
st.set_page_config(page_title="リアル古代魚水槽", layout="wide")

# --- 背景動画を固定するための関数 ---
# ボタンを押しても消えないよう、関数外（メインフロー）で常に呼び出されるようにします
def display_background_video(video_path):
    try:
        with open(video_path, 'rb') as f:
            data = f.read()
        b64 = base64.b64encode(data).decode()
        # st.empty() を使わず、直接ヘッダー付近に埋め込むことで固定します
        st.markdown(f"""
            <style>
            .stApp {{
                background-color: rgba(0,0,0,0);
            }}
            #myVideo {{
                position: fixed;
                right: 0;
                bottom: 0;
                min-width: 100%; 
                min-height: 100%;
                z-index: -2; /* 魚群(z-index: 9999)より奥、UIより奥 */
                object-fit: cover;
            }}
            </style>
            <video autoplay loop muted playsinline id="myVideo">
                <source src="data:video/mp4;base64,{b64}" type="video/mp4">
            </video>
        """, unsafe_allow_html=True)
    except:
        st.error("動画ファイルが見つかりません。")

# 1. 最初に動画を表示（これはボタン操作に関わらず毎回実行されます）
display_background_video('ancient_aquarium.mp4')

st.title("🏛️ リアル・デボン紀アクアリウム")

# 2. サイドバー設定
with st.sidebar:
    st.header("水槽管理パネル")
    btn_fish = st.button("🐟 魚群")

# 3. 魚群ボタンが押された時の処理
if btn_fish:
    fish_icons = ["🐟", "🐠", "🐡", "🦈"]
    fishes_html = ""
    run_id = int(time.time() * 1000)
    animation_name = f"swim_left_{run_id}"
    
    # 魚群専用のスタイル（動画とは別に定義）
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
        z-index: 9999; /* 動画より手前に表示 */
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
    
    # 魚群だけを追加で描画（動画のHTMLとは干渉しません）
    st.markdown(style_html + fishes_html, unsafe_allow_html=True)
