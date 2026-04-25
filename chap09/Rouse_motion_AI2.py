# AIによるRouseモデルのシミュレーション（緩和）
# 精査してないので後日チェック

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- 1. 設定 ---
N = 30
dt = 0.05
zeta = 1.0
k = 2.0
T = 0.3
external_force_mag = 2.0  # 外場の強さ（x方向）
switch_frame = 50         # 50フレーム目で外場をオフにする

# 初期位置：適当な配置
r = np.zeros((N, 2))
r[:, 0] = np.linspace(-5, 5, N) # 最初は直線状に配置

# --- 2. 描画準備 ---
fig, ax = plt.subplots(figsize=(6, 6))
line, = ax.plot([], [], 'o-', lw=2, markersize=4, color='orangered')
title = ax.set_title("")
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.set_aspect('equal')

def update(frame):
    global r
    f_spring = np.zeros_like(r)
    
    # バネの力
    f_spring[1:-1] = -k * (2 * r[1:-1] - r[:-2] - r[2:])
    f_spring[0] = -k * (r[0] - r[1])
    f_spring[-1] = -k * (r[-1] - r[-2])
    
    # 外場の計算 (switch_frame以前はx方向に力を加える)
    f_ext = np.zeros_like(r)
    if frame < switch_frame:
        # 両端を逆方向に引っ張る（伸長）
        f_ext[0, 0] = -external_force_mag
        f_ext[-1, 0] = external_force_mag
        status = "Stretching..."
    else:
        status = "Relaxing..."
    
    # 熱的なランダム力
    f_random = np.random.normal(0, np.sqrt(2 * zeta * T / dt), (N, 2))
    
    # 位置の更新
    r += (f_spring + f_ext + f_random) * dt / zeta
    
    # 重心固定（可視化用）
    r_center = r - np.mean(r, axis=0)
    
    line.set_data(r_center[:, 0], r_center[:, 1])
    title.set_text(f"Frame: {frame} | {status}")
    return line, title

ani = FuncAnimation(fig, update, frames=250, interval=40, blit=True)
plt.show()
