import streamlit as st
import numpy as np
import time
from PIL import Image, ImageDraw

# 設定
st.set_page_config(page_title="リアル古代魚アクアリウム", layout="wide")
st.title("🏛️ 古生代アクアリウム・シミュレーター")

WIDTH, HEIGHT = 800, 450

class AncientFish:
    def __init__(self, name, size, speed, color, count):
        self.name = name
        self.size = size
        self.color = color
        self.fishes = []
        for _ in range(count):
            self.fishes.append({
                "x": np.random.rand() * WIDTH,
                "y": np.random.rand() * HEIGHT,
                "speed": np.random.uniform(speed * 0.8, speed * 1.2),
                "angle": np.random.uniform(0, 2 * np.pi),
                "wave": np.random.uniform(0, 100)
            })

    def update(self):
        for f in self.fishes:
            f["wave"] += 0.2
            # 泳ぐ動きに「しなり」を加える
            f["angle"] += np.sin(f["wave"]) * 0.05
            f["x"] += np.cos(f["angle"]) * f["speed"]
            f["y"] += np.sin(f["angle"]) * f["speed"]

            # 画面端のループ処理
            if f["x"] > WIDTH + 50: f["x"] = -50
            if f["x"] < -50: f["x"] = WIDTH + 50
            if f["y"] > HEIGHT + 50: f["y"] = -50
            if f["y"] < -50: f["y"] = HEIGHT + 50

    def draw(self, draw_obj):
        for f in self.fishes:
            w = self.size
            h = w * 0.4
            # 進行方向に合わせて反転を計算
            direction = 1 if np.cos(f["angle"]) > 0 else -1
            
            # 魚の体（楕円）
            x0, y0 = f["x"] - w/2, f["y"] - h/2
            x1, y1 = f["x"] + w/2, f["y"] + h/2
            draw_obj.ellipse([x0, y0, x1, y1], fill=self.color, outline="white")
            
            # 尾びれ（三角形）
            tx = f["x"] - (w/2 * direction)
            draw_obj.polygon([
                (tx, f["y"]),
                (tx - (20 * direction), f["y"] - 15),
                (tx - (20 * direction), f["y"] + 15)
            ], fill=self.color)
            
            # 目
            ex = f["x"] + (w/3 * direction)
            draw_obj.ellipse([ex-2, f["y"]-5, ex+2, f["y"]-1], fill="black")

# セッション状態での保持
if 'fish_groups' not in st.session_state:
    st.session_state.fish_groups = [
        AncientFish("大：ダンクルオステウス", 120, 1.2, "#4a4a4a", 1),
        AncientFish("中：ユーステノプテロン", 60, 2.0, "#8b4513", 2),
        AncientFish("小：プテラスピス", 30, 3.5, "#d4af37", 3)
    ]

# メインループ
placeholder = st.empty()
bg_choice = st.sidebar.selectbox("水槽の雰囲気", ["深海", "浅瀬", "ナイト"])

bgs = {"深海": "#001f3f", "浅瀬": "#0074d9", "ナイト": "#000010"}

while True:
    # キャンバス作成
    img = Image.new("RGB", (WIDTH, HEIGHT), bgs[bg_choice])
    draw = ImageDraw.Draw(img)
    
    # 泡の演出（ランダム）
    for _ in range(5):
        bx, by = np.random.rand()*WIDTH, np.random.rand()*HEIGHT
        draw.ellipse([bx, by, bx+2, by+2], fill="white")

    # 魚の更新と描画
    for group in st.session_state.fish_groups:
        group.update()
        group.draw(draw)

    placeholder.image(img, use_column_width=True)
    time.sleep(0.05)
