import matplotlib.pyplot as plt
import math
#линейные уравнения (вообще это квадратные уравнения). Строго по опредлению: у линейного уравнения полна степень составляющих многочленов равна 1. Но так как таковых уравнений нет, а есть только квадратные, то будем называть их линейными за отсутствием собственно линейных.
x_lin = list(range(-20,20))
y1 = [i**2 + 2*i + 1 for i in x_lin]
y2 = [-i**2 - 0.5*i for i in x_lin]

#логарифмические уравнения
x_log = list(range(1, 11))
y3=[math.log2(i) for i in x_log]
y4 = [math.log(math.pi*i, math.e) for i in x_log]

#экспоненциальные уравнения
y5 = [math.e**i + 2*i for i in x_lin]
y6 = [math.e**(-2*i) for i in x_lin]

# тригонометрические уравнения
y7=[math.cos(3*i) for i in x_lin]
y8 = [math.sin(i) for i in x_lin]
# # общий график
fig = plt.figure(dpi=200)
ax = fig.add_axes((0.1, 0.1, 0.8,0.8))
ax_lin1 = plt.plot(x_lin,y1, color='b', lw=1, marker='o', markerfacecolor='w', alpha=0.7)
ax_lin2 = plt.plot(x_lin,y2, color='b', lw=1, marker='o', markerfacecolor='w', alpha=0.7)

ax_log1 = plt.plot(x_log,y3, color='g', alpha=0.7)
ax_log2 = plt.plot(x_log,y4, color='g', alpha=0.7)

ax_exp1 = plt.plot(x_lin,y5, color='r', alpha=0.7)
ax_exp2 = plt.plot(x_lin,y6, color='r', alpha=0.7)

ax_trig1 = plt.plot(x_lin,y7, color='k', alpha=0.7)
ax_trig2 = plt.plot(x_lin,y8, color='k', alpha=0.7)
plt.legend([f'y(x)=x{chr(0x00B2)}+2x+1',f'y(x)=-x{chr(0x00B2)}-0,5x', f'y(x) = log2(x)', f'y(x) = ln(pi*x)', f'у(x)= e{chr(0x000002E3)}+2x', f'у(x)= e^(-2x)', f'y(x) = cos(3x)', f'y(x) = sin(x)'], loc='best')

ax.grid(color='#f74b6d', ls='--', alpha=0.6)
ax.set_ylim(-15, 15)
ax.set_title('График со всеми типами функций')
plt.show()
#
# #линейные уравнения
x_lin = list(range(-20,20))
y1 = [i**2 + 2*i + 1 for i in x_lin]
y2 = [-i**2 - 0.5*i for i in x_lin]
fig = plt.figure(dpi=200, facecolor='#f1efea')
ax = fig.add_axes((0.1, 0.1, 0.8,0.8), facecolor='#d4e8fa')
ax1 = plt.plot(x_lin,y1, color='blue', alpha=0.45, marker='o', markerfacecolor='w', markeredgewidth=1.5, ls='-.')
ax2 = plt.plot(x_lin,y2, color=(0.824, 0.071, 0.91), alpha=0.7, marker='o', markerfacecolor='w', markeredgewidth=1.5, lw=3)
ax.set_ylim(-50, 50)
ax.set_title('Линейные уравнения', fontstyle='italic', fontweight='bold', color='k', fontsize=10)
ax.set_xlabel('Значения Х', fontsize=9)
ax.set_ylabel('Значения Y', fontsize=9)
ax.grid(color='#f74b6d', ls='--', alpha=0.6)
plt.legend([f'y(x)=x{chr(0x00B2)}+2x+1',f'y(x)=-x{chr(0x00B2)}-0,5x'], loc='best', facecolor='#fedcaf', edgecolor='#f53f3f')
plt.show()
# #
# #логарифмические уравнения
x_log = list(range(1,50))
y3=[math.log2(i) for i in x_log]
y4 = [math.log(math.pi*i, math.e) for i in x_log]
fig = plt.figure(dpi=200, facecolor='#f1efea')
ax = fig.add_axes((0.1, 0.1, 0.8,0.8), facecolor='#d4e8fa')
ax1 = plt.plot(x_log,y3, color='blue', alpha=0.45, marker='o', markerfacecolor='w', markeredgewidth=1.5, ls='-.')
ax2 = plt.plot(x_log,y4, color=(0.824, 0.071, 0.91), alpha=0.7, marker='o', markerfacecolor='w', markeredgewidth=1.5, lw=3)
ax.set_ylim(-50, 50)
ax.set_title('Логарифмические уравнения', fontstyle='italic', fontweight='bold', color='k', fontsize=10)
ax.set_xlabel('Значения Х', fontsize=9)
ax.set_ylabel('Значения Y', fontsize=9)
ax.grid(color='#f74b6d', ls='--', alpha=0.6)
plt.legend([f'y(x) = log2(x)', f'y(x) = ln(pi*x)'], loc='best', facecolor='#fedcaf', edgecolor='#f53f3f')
# plt.show()
#
# #экспоненциальные уравнения
x_lin = list(range(-20,20))
y5 = [math.e**i + 2*i for i in x_lin]
y6 = [math.e**(-2*i) for i in x_lin]
fig = plt.figure(dpi=200, facecolor='#f1efea')
ax = fig.add_axes((0.1, 0.1, 0.8,0.8), facecolor='#d4e8fa')
ax1 = plt.plot(x_lin,y5, color='blue', alpha=0.45, marker='o', markerfacecolor='w', markeredgewidth=1.5, ls='-.')
ax2 = plt.plot(x_lin,y6, color=(0.824, 0.071, 0.91), alpha=0.7, marker='o', markerfacecolor='w', markeredgewidth=1.5, lw=3)
ax.set_ylim(-50, 50)
ax.set_title('Экспоненциальные уравнения', fontstyle='italic', fontweight='bold', color='k', fontsize=10)
ax.set_xlabel('Значения Х', fontsize=9)
ax.set_ylabel('Значения Y', fontsize=9)
ax.grid(color='#f74b6d', ls='--', alpha=0.6)
plt.legend([f'у(x)= e{chr(0x000002E3)}+2x', f'у(x)= e^(-2x)'], loc='best', facecolor='#fedcaf', edgecolor='#f53f3f')
plt.show()

# тригонометрические уравнения
x_lin1 = list(range(-30,30))
y7=[math.cos(3*i) for i in x_lin1]
y8 = [math.sin(i) for i in x_lin1]
fig = plt.figure(dpi=200, facecolor='#f1efea')
ax = fig.add_axes((0.1, 0.1, 0.8,0.8), facecolor='#d4e8fa')
ax1 = plt.plot(x_lin1,y7, color='r', alpha=0.45, marker='p', markerfacecolor='w', markeredgewidth=1.5, ls='-')
ax2 = plt.plot(x_lin1, y8, color='g', alpha=0.7, marker='o', markerfacecolor='w', markeredgewidth=1.5, lw=3)
ax.set_ylim(-3, 3)
ax.set_title('Тригонометрические уравнения', fontstyle='italic', fontweight='bold', color='k', fontsize=10)
ax.set_xlabel('Значения Х', fontsize=9)
ax.set_ylabel('Значения Y', fontsize=9)
ax.grid(color='#f74b6d', ls='--', alpha=0.6)
plt.legend([f'y(x) = cos(3x)', f'y(x) = sin(x)'], loc='best', facecolor='#fedcaf', edgecolor='#f53f3f')
plt.show()