import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 緩和弾性率の定義
def relaxation_modulus(t_elapsed, G_inf=1.0, G1=2.0, tau=3.0):
    return np.where(t_elapsed >= 0, G_inf + G1 * np.exp(-t_elapsed/tau), 0)

# 1. データ準備
t = np.linspace(0, 20, 400)
t1, t2 = 2.0, 10.0  # ステップ歪みを加える時刻
stress1 = 1.0 * relaxation_modulus(t - t1)
stress2 = 1.0 * relaxation_modulus(t - t2)
stress_total = stress1 + stress2

# 2. グラフの初期設定
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7), sharex=True)

# --- 上段：歪み (Input) ---
ax1.set_xlim(0, 20)
ax1.set_ylim(-0.2, 2.5) # 縦軸を固定
ax1.set_ylabel('Applied Strain')
ax1.set_title('Boltzmann Superposition (Strees Relaxation)')
ax1.grid(True, ls='--')
line_strain, = ax1.step([], [], where='post', color='black', lw=2)

# --- 下段：応力 (Response) ---
ax2.set_xlim(0, 20)
ax2.set_ylim(-0.2, 5.0) # 縦軸を固定
ax2.set_xlabel('Time (Absolute)')
ax2.set_ylabel('Stress')
ax2.grid(True, ls='--')

line_s1, = ax2.plot([], [], 'b--', alpha=0.5, label='Response to Step 1 (t=2)')
line_s2, = ax2.plot([], [], 'g--', alpha=0.5, label='Response to Step 2 (t=10)')
line_total, = ax2.plot([], [], 'r-', lw=2.5, label='Total Stress (Sum)')
ax2.legend(loc='upper right')

# 3. アニメーション更新関数
def animate(i):
    curr_t = t[:i]
    # 歪みデータの更新
    strain_history = np.where(curr_t < t1, 0, np.where(curr_t < t2, 1.0, 2.0))
    line_strain.set_data(curr_t, strain_history)
    
    # 応力データの更新
    line_s1.set_data(t[:i], stress1[:i])
    line_s2.set_data(t[:i], stress2[:i])
    line_total.set_data(t[:i], stress_total[:i])
    return line_strain, line_s1, line_s2, line_total

# アニメーション実行
ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=25, blit=True)

ani.save('./gif/Boltzmann_superposition_relaxation.gif', dpi=300)

plt.tight_layout()
plt.show()
