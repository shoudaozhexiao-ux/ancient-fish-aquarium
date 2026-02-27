import streamlit as st
import numpy as np
import time
from PIL import Image, ImageDraw, ImageFilter

# --- 設定 ---
st.set_page_config(page_title="リアル古代魚水槽 v2", layout="wide")
st.title("🏛️ リアル・エキゾチック・アクアリウム")

# 水槽のサイズ
WIDTH, HEIGHT = 900, 550

# --- 魚のクラス定義 ---
class RealisticFish:
    def __init__(self, name, size, speed, color_back, color_belly, pattern_color, count):
        self.name = name
        self.size = size
        self.color_back = color_back
        self.color_belly = color_belly
        self.pattern_color = pattern_color
        self.fishes = []
        for _ in range(count):
            self.fishes.append({
                "x": np.random.rand() * WIDTH,
                "y": np.random.rand() * HEIGHT,
                "speed": np.random.uniform(speed * 0.8, speed * 1.2),
                "angle": np.random.uniform(0, 2 * np.pi),
                "phi": np.random.uniform(0, 100) # 尾びれ用周期
            })

    def update(self):
        for f in self.fishes:
            # 物理計算：しなやかな動きと旋回
            f["phi"] += 0.15
            f["angle"] += Math.sin(f["phi"] * 0.2) * 0.05
            
            # 壁回避のソフト旋回
            margin = 80
            if(f["x"] < margin or f["x"] > WIDTH-margin or f["y"] < margin or f["y"] > HEIGHT-margin):
                f["angle"] += 0.15

            # 移動
            f["x"] += Math.cos(f["angle"]) * f["speed"]
            f["y"] += Math.sin(f["angle"]) * f["speed"]

    def draw(self, canvas_draw):
        for f in self.fishes:
            # 魚の体を描く (ベジェ曲線とグラデーション)
            w = this.size
            h = w * 0.4
            
            canvas_draw.save()
            canvas_draw.translate(f["x"], f["y"])
            canvas_draw.rotate(f["angle"])
            if (f["vx"] < 0) canvas_draw.scale(1, -1); # 進行方向で反転

            # 1. 尾びれ (透明感のあるグラデーション)
            tailWag = Math.sin(f["phi"]) * 0.3;
            canvas_draw.beginPath();
            canvas_draw.fillStyle = this.c1;
            canvas_draw.globalAlpha = 0.6;
            canvas_draw.moveTo(w * 0.4, 0);
            canvas_draw.lineTo(w * 0.8, -h * 0.6 + tailWag * 10);
            canvas_draw.lineTo(w * 0.6, tailWag * 10);
            canvas_draw.lineTo(w * 0.8, h * 0.6 + tailWag * 10);
            canvas_draw.fill();

            # 2. 体 (複雑な階層描画)
            canvas_draw.globalAlpha = 1.0;
            const grad = canvas_draw.createLinearGradient(0, -h/2, 0, h/2);
            grad.addColorStop(0, this.c2); // 背中
            grad.addColorStop(0.5, this.c1); // 中央
            grad.addColorStop(1, '#FFF'); // お腹
            canvas_draw.fillStyle = grad;
            
            canvas_draw.beginPath();
            canvas_draw.moveTo(-w * 0.5, 0); // 鼻先
            canvas_draw.bezierCurveTo(-w*0.3, -h*0.7, w*0.2, -h*0.6, w*0.4, 0); // 背中
            canvas_draw.bezierCurveTo(w*0.2, h*0.6, -w*0.3, h*0.7, -w*0.5, 0); // お腹
            canvas_draw.fill();

            # 3. 特徴的な模様
            canvas_draw.globalAlpha = 0.3;
            canvas_draw.fillStyle = this.c2;
            if(this.id === 0) { // テトラの赤い線
                canvas_draw.fillRect(-w*0.2, 0, w*0.5, h*0.2);
            }
            if(this.id === 3) { // アロワナの鱗
                canvas_draw.strokeStyle = "rgba(255,215,0,0.3)";
                for(let i=0; i<5; i++) {
                    canvas_draw.strokeRect(-w*0.2 + i*10, -h*0.2, 5, h*0.4);
                }
            }

            # 4. 目 (生命感を宿す)
            canvas_draw.globalAlpha = 1.0;
            canvas_draw.fillStyle = "white";
            canvas_draw.beginPath(); canvas_draw.arc(-w * 0.35, -h * 0.1, h * 0.2, 0, Math.PI * 2); canvas_draw.fill();
            canvas_draw.fillStyle = "black";
            canvas_draw.beginPath(); canvas_draw.arc(-w * 0.37, -h * 0.1, h * 0.1, 0, Math.PI * 2); canvas_draw.fill();

            canvas_draw.restore();

// --- 初期化 ---
if 'aquarium' not in st.session_state:
    # 魚のリスト作成（実在する魚のカラー）
    st.session_state.fish_groups = [
        RealisticFish("カージナルテトラ(小)", 35, 2.2, '#40E0D0', '#FF0000', '#FFFFFF', 5),
        RealisticFish("キイロハギ(中)", 70, 1.4, '#FFFF00', '#FFFFCC', '#FFFF00', 3),
        RealisticFish("ラスボラ(小)", 25, 2.8, '#FFCC99', '#444444', '#FFDDCC', 8),
        RealisticFish("アジアアロワナ(大)", 160, 1.0, '#C0C0C0', '#A0A0A0', '#FFD700', 1)
    ]
    st.session_state.aquarium = True

# --- メインループ ---
placeholder = st.empty()

# 背景の設定
st.sidebar.markdown("### 水槽の設定")
bg_type = st.sidebar.selectbox("背景変更", ["深海", "サンゴ礁", "淡水・川", "夕暮れ", "漆黒"])

bgs = {
    "深海": ('#10304a', '#050a0f'),
    "サンゴ礁": ('#4ca1af', '#2c3e50'),
    "淡水・川": ('#556b2f', '#111100'),
    "夕暮れ": ('#ff5f6d', '#ffc371'),
    "漆黒": ('#000', '#000')
}

while True:
    # キャンバス（背景）の作成
    canvas = Image.new("RGB", (WIDTH, HEIGHT), bgs[bg_type][0])
    draw = ImageDraw.Draw(canvas)
    
    # 魚の更新と描画
    for group in st.session_state.fish_groups:
        group.update()
        group.draw(draw)

    # わずかなブラー効果でリアルさを演出
    processed_canvas = canvas.filter(ImageFilter.GaussianBlur(radius=0.5))

    # 表示を更新
    placeholder.image(processed_canvas, use_column_width=True)
    
    # フレームレート調整
    time.sleep(0.05)
