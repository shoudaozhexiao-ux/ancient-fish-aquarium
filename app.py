import streamlit as st
import base64
import random

# ページの設定
st.set_page_config(page_title="リアル古代魚水槽", layout="wide")

# 背景動画を設定し、魚群アニメーションの「型」を定義するHTML
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
        
        /* 魚群アニメーションの定義 */
        @keyframes swim_left {{
            from {{ transform: translateX(105vw); }}
            to {{ transform: translateX(-150vw); }}
        }}
        .fish {{
            position: fixed; pointer-events: none; z-index: 9999;
            animation: swim_left 3s linear forwards;
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
    st.error("動画が見つかりません。")

st.title("🏛️ リアル・デボン紀アクアリウム")

# サイドバー設定
with st.sidebar:
    st.header("水槽管理パネル")
    btn_fish = st.button("🐟 魚群")

# 魚群ボタンが押された時の処理
if btn_fish:
    # 魚群を生成するHTML（コードが表示されないよう、コンポーネントとして実行）
    fish_icons = ["🐟", "🐠", "🐡", "🦈"]
    fishes = ""
    for i in range(80):  # 80匹に増量！
        top = random.randint(0, 95)
        delay = random.uniform(0, 2.0)
        speed = random.uniform(2.0, 4.0)
        size = random.randint(20, 60)
        icon = random.choice(fish_icons)
        fishes += f'<div class="fish" style="top:{top}%; left:100%; animation-delay:{delay}s; animation-duration:{speed}s; font-size:{size}px;">{icon}</div>'
    
    # ここがポイント：st.componentsを使ってHTMLとして確実に実行させる
    st.components.v1.html(f"""
        <div id="fish-container">
            {fishes}
        </div>
        <script>
            // 一定時間後に要素を消してメモリを節約
            setTimeout(() => {{
                document.getElementById('fish-container').remove();
            }}, 6000);
        </script>
    """, height=0) # height=0にすることで、余計な余白やコード表示を防ぎます
