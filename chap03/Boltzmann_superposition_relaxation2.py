import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 緩和弾性率 G(t)
def relaxation_modulus(t_elapsed, G_inf=1.0, G1=3.0, tau=3.0):
    return np.where(t_elapsed >= 0, G_inf + G1 * np.exp(-t_elapsed/tau), 0)

# 1. データ設定
t = np.linspace(0, 25, 500)
t_on, t_off = 2.0, 12.0  # 歪みを与える時刻と、取り除く時刻
strain_val = 1.0

# 重ね合わせの計算
# 歪みを取り除く = 「マイナスの歪みを加える」と考える
stress_on = strain_val * relaxation_modulus(t - t_on)
stress_off = -strain_val * relaxation_modulus(t - t_off) # 逆向きの応答
stress_total = stress_on + stress_off

# 2. グラフ設定
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7), sharex=True)

# 軸の固定
ax1.set_xlim(0, 25)
ax1.set_ylim(-0.2, 1.5)
ax1.set_ylabel('Applied Strain')
ax1.set_title('Stress Relaxation: Loading & Unloading')
ax1.grid(True, ls='--')
line_strain, = ax1.step([], [], where='post', color='black', lw=2)

ax2.set_xlim(0, 25)
ax2.set_ylim(-4.5, 4.5)
ax2.set_xlabel('Time (Absolute)')
ax2.set_ylabel('Stress')
ax2.grid(True, ls='--')

line_s_on, = ax2.plot([], [], 'b--', alpha=0.5, label='Response to Load (t=2)')
line_s_off, = ax2.plot([], [], 'g--', alpha=0.5, label='Response to Unload (t=12)')
line_total, = ax2.plot([], [], 'r-', lw=2.5, label='Total Stress (Sum)')
ax2.legend(loc='upper right')

# 3. 更新関数
def animate(i):
    curr_t = t[:i]
    # 歪み履歴 (t_onで1になり、t_offで0に戻る)
    strain_history = np.where(curr_t < t_on, 0, np.where(curr_t < t_off, strain_val, 0))
    line_strain.set_data(curr_t, strain_history)
    
    line_s_on.set_data(t[:i], stress_on[:i])
    line_s_off.set_data(t[:i], stress_off[:i])
    line_total.set_data(t[:i], stress_total[:i])
    return line_strain, line_s_on, line_s_off, line_total

ani = animation.FuncAnimation(fig, animate, frames=len(t), interval=20, blit=True)

ani.save('./gif/Boltzmann_superposition_relaxation2.gif', dpi=300)

plt.tight_layout()
plt.show()
