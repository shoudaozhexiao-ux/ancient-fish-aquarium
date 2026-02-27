import streamlit as st
import base64

# ページ設定
st.set_page_config(page_title="古生代シミュレーター", layout="wide")

def get_base64_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_bg_video(video_file):
    bin_str = get_base64_bin_file(video_file)
    # CSSを使って動画を背景に固定する魔法のコード
    footer_style = f"""
    <style>
    #MainCanvas {{
        display: none;
    }}
    .stApp {{
        background: none;
    }}
    #video-bg {{
        position: fixed;
        right: 0;
        bottom: 0;
        min-width: 100%; 
        min-height: 100%;
        z-index: -1;
        filter: brightness(0.7); /* 少し暗くして文字を見やすく */
    }}
    </style>
    <video autoplay loop muted playsinline id="video-bg">
        <source src="data:video/mp4;base64,{bin_str}" type="video/mp4">
    </video>
    """
    st.markdown(footer_style, unsafe_allow_html=True)

# 動画背景の適用（ファイル名が一致している必要があります）
try:
    set_bg_video('ancient_aquarium.mp4')
except FileNotFoundError:
    st.error("動画ファイル 'ancient_aquarium.mp4' が見つかりません。GitHubにアップロードしてください。")

# UIレイヤー（動画の上に重なるメニュー）
st.title("🏛️ リアル・デボン紀アクアリウム")
st.write("3億8千万年前の海を、最高画質のシミュレーションで再現しています。")

with st.sidebar:
    st.header("水槽管理パネル")
    st.info("現在は『デボン紀：ダンクルオステウスの時代』を表示中。")
    if st.button("エサをあげる"):
        st.balloons()
        st.success("エサを投げ入れました！（魚たちが反応する演出をシミュレート中）")

    st.markdown("---")
    st.write("💡 **ヒント**")
    st.caption("この水槽は、Pythonと最新の映像処理技術を組み合わせて配信されています。")
