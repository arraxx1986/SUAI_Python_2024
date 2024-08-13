import matplotlib.pyplot as plt
import math
x = list(range(-10,11))
y1 = [i**2 + 2*i + 1 for i in x]
y2 = [i**2 - 0.5*i for i in x]
y3 = [math.e**i + 2*i for i in x]
fig = plt.figure(dpi=200, facecolor='#f1efea')
ax = fig.add_axes((0.1, 0.1, 0.8,0.8), facecolor='#d4e8fa')
ax1 = plt.plot(x,y1, color='blue', alpha=0.45, marker='o', markerfacecolor='w', markeredgewidth=1.5, ls='-.')
ax2 = plt.plot(x,y2, color=(0.824, 0.071, 0.91), alpha=0.7, marker='o', markerfacecolor='w', markeredgewidth=1.5, lw=3)
ax3 = plt.plot(x,y3, color='#eb9e10', alpha=0.95, marker='o', markerfacecolor='w', markeredgewidth=1.5, ls='--')
ax.set_ylim(-25, 150)# специально ограничиваю верхнюю границу по оси Оу, так как значения третьей функции при х от [-10, 10] уходят до 22000. При этом остальные две функции имеют куда меньшие значения по оси Оу при максимальном значении х.
ax.set_xticks([i for i in x if i % 2 == 0])
ax.set_title('Задание № 1 Золотых Д.С.', fontstyle='italic', fontweight='bold', color='k', fontsize=10)
ax.set_xlabel('Значения Х', fontsize=9)
ax.set_ylabel('Значения Y', fontsize=9)
ax.grid(color='#f74b6d', ls='--', alpha=0.6)
plt.legend([f'y(x)=x{chr(0x00B2)}+2x+1',f'y(x)=x{chr(0x00B2)}-0,5x',f'у(x)= e{chr(0x000002E3)}+2x'], loc=(0.3, 0.81), facecolor='#fedcaf', edgecolor='#f53f3f')
fig.savefig('Задание №1 Золотых Д.С..jpeg')
plt.show()
