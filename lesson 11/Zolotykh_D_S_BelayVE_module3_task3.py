import re
import matplotlib.pyplot as plt
def string_to_list_x_and_y():
    s = input()
    lst = list(re.split(r'[.,:;!-?\s]+', s))#вот тут подсмотрел на сайтах, так как с модулем re я не знаком.
    if len(lst[-1]) == 0:
        lst.pop(-1)
    lst_length = [len(i) for i in lst]
    return [lst, lst_length]

data = string_to_list_x_and_y()
x = data[0].copy()
y = data[1].copy()
fig = plt.figure(dpi = 150)
ax = fig.add_axes([0.05,0.2,0.9,0.75])
ax1 = ax.plot(x,y, marker='o')
ax.grid(color='grey', alpha=0.7, ls='--')
plt.yticks(y)
ax.tick_params(labelrotation=45)
plt.show()


