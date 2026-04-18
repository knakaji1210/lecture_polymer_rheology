# Rouseモデルのアニメーション(2d)、解を描画するだけのバージョン
# 1dのRouseモデルのアニメーションを、xとyの両方で描画するバージョン（不完全かもしれない）

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Rouseモデルのパラメータの設定
N = 100  # モノマー数
n = np.linspace(0, N, N+1)  # セグメント番号

P = 5  # 描画する固有モード数
p = np.arange(1, P + 1)  # 固有モード番号

amp_x_p = [random.uniform(0.5, 1.0) for _ in p]  # 各モードの振幅（0.5から1.0の間でランダムに生成）
amp_y_p = [random.uniform(0.5, 1.0) for _ in p]  # 各モードの振幅（0.5から1.0の間でランダムに生成）

tau_R = 1.0  # Rouse緩和時間（これでスケールしたことにする）
tau_p = tau_R / (2 * p ** 2)  # 各モードの緩和時間

# データの準備
x = np.pi * n / N                   # セグメント位置（x座標）
y = np.pi * n / N                   # セグメント位置（y座標）
t = np.linspace(0, tau_R * 1.5, 500)  # 時間tの刻み（アニメーションのフレーム数）

# 関数定義
def rouse_x(x, p, i):
    j=i-1
    return amp_x_p[j] * np.cos(p[j] * x)
def rouse_y(y, p, i):
    j=i-1
    return amp_y_p[j] * np.cos(p[j] * y)
def rouse_t(t, p, i):
    j=i-1
    return np.exp(-t / tau_p[j])

def rouse_x_solution(x, t, p):
    rouse_x_modes = np.zeros_like(x)
    for i in p:
        rouse_x_modes += rouse_x(x, p, i) * rouse_t(t, p, i)  # 各モードの寄与を加算
    return rouse_x_modes

def rouse_y_solution(y, t, p):
    rouse_y_modes = np.zeros_like(y)
    for i in p:
        rouse_y_modes += rouse_y(y, p, i) * rouse_t(t, p, i)  # 各モードの寄与を加算
    return rouse_y_modes

# グラフの初期設定
title = r'Rouse model (2d) ($N$ = {0:.0f}, $p_{{max}}$ = {1:.0f})'.format(N, P)
xlabel = r'x-Displacement of Beads'
ylabel = r'y-Displacement of Beads'
savefile = './gif/Rouse_solution_2d_N{0:.0f}_Pmax{1:.0f}.gif'.format(N, P)

fig = plt.figure(figsize=(8,5), tight_layout=True) 
ax = fig.add_subplot(111)
ax.set_title(title)
ax.set_xlabel(xlabel)
ax.set_ylabel(ylabel)
ax.grid()
ax.set_axisbelow(True)

line, = ax.plot(rouse_x_solution(x, 0, p), rouse_y_solution(y, 0, p), 'b-', linewidth=1, zorder=1) # 初期フレーム
dot = ax.scatter(rouse_x_solution(x, 0, p), rouse_y_solution(y, 0, p), c='red', s=5, zorder=2)  # 動く点（ビーズの位置を示す）

# アニメーション更新関数
def update(frame):
    current_t = t[frame]
    xnew = rouse_x_solution(x, current_t, p)
    ynew = rouse_y_solution(y, current_t, p)
    line.set_data(xnew, ynew)  # xとyの両方を更新
    dot.set_offsets(np.c_[xnew, ynew])  # 点の位置を更新
    return line, dot, 

# アニメーションの作成
ani = animation.FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)

#ani.save(savefile, dpi=300)

plt.show()
