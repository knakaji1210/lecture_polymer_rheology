import numpy as np
import matplotlib.pyplot as plt

frequency = 0.5                 # 周波数 (Hz)
omega = 2 * np.pi * frequency   # 角周波数 (rad/s)

strain_amplitude = 0.01         # ひずみの振幅（無次元）
stress_amplitude = 2 * 10**4    # 応力の振幅（Pa）

t = np.linspace(0, 4, 500)
strain = strain_amplitude * np.cos(omega * t)
stress = stress_amplitude * np.cos(omega * t + np.pi / 6)  # 位相差 π/4 (45度)

fig = plt.figure(figsize=(8, 7), tight_layout=True)
ax1 = fig.add_subplot(211)
ax1.set_title('Dynamic Strain (input frequency = {0:.1f} Hz)'.format(frequency))
ax1.set_xlim(0, 4)
ax1.set_ylim(-2*strain_amplitude, 2*strain_amplitude)
ax1.set_xlabel('Time /s')
ax1.set_ylabel('Strain ($\epsilon$) /')
ax1.grid(True, ls='--')
ax1.plot(t, strain, color='blue', lw=2)
ax2 = fig.add_subplot(212)
ax2.set_title('Dynamic Stress')
ax2.set_xlim(0, 4)
ax2.set_ylim(-2*stress_amplitude, 2*stress_amplitude)
ax2.set_xlabel('Time /s')
ax2.set_ylabel('Stress ($\sigma$) /Pa')
ax2.grid(True, ls='--')
ax2.plot(t, stress, color='red', lw=2)
ax2.vlines(0.833, -2*stress_amplitude, 2*stress_amplitude, color='black', lw=1, ls='--')  # 位相差の目安線
ax2.text(0.90, 0.60, r'$t$ = 0.833 s', fontsize=10)

savefile = './png/Dynamic_modulus.png'
fig.savefig(savefile, dpi=300)

plt.show()