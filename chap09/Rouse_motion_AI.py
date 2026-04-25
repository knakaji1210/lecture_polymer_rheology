# AIによるRouseモデルのシミュレーション（ランダムな動き）
# 精査してないので後日チェック

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- 1. 設定 ---
N = 30
dt = 0.05
zeta = 1.0
k = 3.0
T = 0.5

# 初期位置 (N, 2)
r = np.cumsum(np.random.normal(0, 0.5, (N, 2)), axis=0)

# --- 2. 描画準備 ---
fig, ax = plt.subplots(figsize=(6, 6))
line, = ax.plot([], [], 'o-', lw=2, markersize=4)
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.set_aspect('equal')

def update(frame):
    global r
    # 力の初期化
    f_spring = np.zeros_like(r)
    
    # バネの力：隣接ビーズ間 (フックの法則)
    # 中間のビーズ
    f_spring[1:-1] = -k * (2 * r[1:-1] - r[:-2] - r[2:])
    # 端のビーズ
    f_spring[0] = -k * (r[0] - r[1])
    f_spring[-1] = -k * (r[-1] - r[-2])
    
    # 熱的なランダム力
    f_random = np.random.normal(0, np.sqrt(2 * zeta * T / dt), (N, 2))
    
    # 位置の更新
    r += (f_spring + f_random) * dt / zeta
    
    # 重心を原点に固定（画面外への脱走防止）
    r_center = r - np.mean(r, axis=0)
    
    # 修正箇所: 変数名を r_center に統一
    line.set_data(r_center[:, 0], r_center[:, 1])
    return line,

ani = FuncAnimation(fig, update, frames=200, interval=30, blit=True)
plt.show()
