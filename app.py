import streamlit as st
import base64
import random

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
            
            /* 魚群アニメーション：最初から画面外(110vw)に配置 */
            @keyframes swim_left {{
                0% {{ transform: translateX(0); opacity: 0; }}
                5% {{ opacity: 0.8; }}
                95% {{ opacity: 0.8; }}
                100% {{ transform: translateX(-220vw); opacity: 0; }}
            }}
            .fish {{
                position: fixed; 
                left: 110vw; /* 最初は画面の右外に隠す */
                pointer-events: none; 
                z-index: 9999;
                animation: swim_left 4s linear forwards;
            }}
            </style>
            <video autoplay loop muted playsinline id="myVideo">
                <source src="data:video/mp4;base64,{b64}" type="video/mp4">
            </video>
        """
    except:
        return ""

# 背景動画の表示
base_html = get_base_html('ancient_aquarium.mp4')
if base_html:
    st.markdown(base_html, unsafe_allow_html=True)
else:
    st.error("動画ファイルが見つかりません。")

st.title("🏛️ リアル・デボン紀アクアリウム")

# サイドバー設定
with st.sidebar:
    st.header("水槽管理パネル")
    btn_fish = st.button("🐟 魚群")

# 魚群ボタンが押された時の処理
if btn_fish:
    fish_icons = ["🐟", "🐠", "🐡", "🦈"]
    fishes_html = ""
    # 毎回ユニークなIDを生成して、アニメーションを強制リセット
    unique_id = random.randint(0, 999999)
    
    for i in range(100):
        top = random.randint(0, 95)
        delay = random.uniform(0, 2.5)
        speed = random.uniform(3.0, 5.0)
        size = random.randint(25, 75)
        icon = random.choice(fish_icons)
        # 各魚のスタイルにアニメーションを直接付与
        fishes_html += f'<div class="fish" style="top:{top}%; animation-delay:{delay}s; animation-duration:{speed}s; font-size:{size}px;">{icon}</div>'
    
    # 描画
    st.markdown(f'<div id="tank-{unique_id}">{fishes_html}</div>', unsafe_allow_html=True)
