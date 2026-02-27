import streamlit as st
import numpy as np
import time
from PIL import Image, ImageDraw

# --- 設定 ---
st.set_page_config(page_title="リアル古代魚水槽", layout="wide")
st.title("🏛️ 古生代アクアリウム (Dunkleosteus Era)")

# 水槽のサイズ
WIDTH, HEIGHT = 800, 450

# --- 魚のクラス定義 ---
class AncientFish:
    def __init__(self, name, image_path, size_range, speed_range, count):
        self.name = name
        # 画像の読み込み（画像がない場合でもエラーにならないよう、ダミー画像を作る処理も含む）
        try:
            self.img = Image.open(image_path).convert("RGBA")
        except:
            # 画像がない場合は色のついた楕円で代用（テスト用）
            self.img = Image.new("RGBA", (100, 50), (100, 100, 100, 255))
        
        self.fishes = []
        for _ in range(count):
            size = np.random.randint(*size_range)
            self.fishes.append({
                "x": np.random.rand() * WIDTH,
                "y": np.random.rand() * HEIGHT,
                "speed": np.random.uniform(*speed_range),
                "angle": np.random.uniform(0, 2 * np.pi),
                "size": size,
                "img": self.img.resize((size, int(size * 0.5)), Image.LANCZOS)
            })

    def update(self):
        for f in self.fishes:
            # 物理計算：ランダムな動きと直進
            f["angle"] += np.random.uniform(-0.1, 0.1)
            f["x"] += np.cos(f["angle"]) * f["speed"]
            f["y"] += np.sin(f["angle"]) * f["speed"]

            # 壁に当たったら反対へ（ループ）
            if f["x"] > WIDTH: f["x"] = -f["size"]
            if f["x"] < -f["size"]: f["x"] = WIDTH
            if f["y"] > HEIGHT: f["y"] = -f["size"]
            if f["y"] < -f["size"]: f["y"] = HEIGHT

# --- 初期化 ---
if 'aquarium' not in st.session_state:
    # 魚のリスト作成 (大1, 中2, 小3)
    # ※ 'images/xxx.png' は実際に用意する画像パスに合わせてください
    st.session_state.fish_groups = [
        AncientFish("大：ダンクルオステウス", "images/dunkle.png", (180, 220), (1, 2), 1),
        AncientFish("中：ユーステノプテロン", "images/eusthe.png", (80, 120), (2, 4), 2),
        AncientFish("小：プテラスピス", "images/ptera.png", (40, 60), (4, 6), 3)
    ]
    st.session_state.aquarium = True

# --- メインループ ---
placeholder = st.empty()

# 背景の作成
bg_color = (10, 40, 60) # 深海の青

while True:
    # キャンバス（背景）の作成
    canvas = Image.new("RGB", (WIDTH, HEIGHT), bg_color)
    
    for group in st.session_state.fish_groups:
        group.update()
        for f in group.fishes:
            # 魚の向きに合わせて画像を反転
            current_img = f["img"]
            if np.cos(f["angle"]) < 0:
                current_img = current_img.transpose(Image.FLIP_LEFT_RIGHT)
            
            # 画像の合成
            canvas.paste(current_img, (int(f["x"]), int(f["y"])), current_img)

    # 表示を更新
    placeholder.image(canvas, use_column_width=True)
    
    # フレームレート調整（0.05秒待機 = 約20fps）
    time.sleep(0.05)
