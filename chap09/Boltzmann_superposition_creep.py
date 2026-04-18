import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# クリープコンプライアンスの定義 (J(t): 単位応力あたりの歪み)
def creep_compliance(t_elapsed, J0=0.5, J1=1.5, tau=4.0):
    # J0: 即時弾性、J1: 遅延弾性の強さ、tau: 遅延時間
    return np.where(t_elapsed >= 0, J0 + J1 * (1 - np.exp(-t_elapsed/tau)), 0)

# 1. データ準備
t = np.linspace(0, 25, 500)
t1, t2 = 2.0, 12.0  # 荷重（応力）を加える時刻
stress_step = 1.0   # 各ステップでの荷重の大きさ

# 各荷重による個別の歪み応答
strain1 = stress_step * creep_compliance(t - t1)
strain2 = stress_step * creep_compliance(t - t2)
strain_total = strain1 + strain2

# 2. グラフの初期設定
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7), sharex=True)

# --- 上段：応力 (Input) ---
ax1.set_xlim(0, 25)
ax1.set_ylim(-0.2, 2.5) # 縦軸固定
ax1.set_ylabel('Applied Stress ($\sigma$)')
ax1.set_title('Boltzmann Superposition (Creep)')
ax1.grid(True, ls='--')
line_stress, = ax1.step([], [], where='post', color='black', lw=2)

# --- 下段：歪み (Response) ---
ax2.set_xlim(0, 25)
ax2.set_ylim(-0.2, 5.0) # 縦軸固定
ax2.set_xlabel('Time (Absolute)')
ax2.set_ylabel('Strain ($\epsilon$)')
ax2.grid(True, ls='--')

line_str1, = ax2.plot([], [], 'b--', alpha=0.5, label='Creep from Step 1 (t=2)')
line_str2, = ax2.plot([], [], 'g--', alpha=0.5, label='Creep from Step 2 (t=12)')
line_total, = ax2.plot([], [], 'r-', lw=2.5, label='Total Strain (Sum)')
ax2.legend(loc='upper left')

# 3. アニメーション更新関数
def animate(i):
    curr_t = t[:i]
    # 応力履歴の更新
    stress_history = np.where(curr_t < t1, 0, np.where(curr_t < t2, stress_step, stress_step * 2))
    line_stress.set_data(curr_t, stress_history)
    
    # 歪みデータの更新
    line_str1.set_data(t[:i], strain1[:i])
    line_str2.set_data(t[:i], strain2[:i])
    line_total.set_data(t[:i], strain_total[:i])
    return line_stress, line_str1, line_str2, line_total

# アニメーション実行
ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=20, blit=True)

ani.save('./gif/Boltzmann_superposition_creep.gif', dpi=300)

plt.tight_layout()
plt.show()
