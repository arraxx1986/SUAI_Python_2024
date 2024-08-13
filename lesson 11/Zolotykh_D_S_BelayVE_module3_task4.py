import re
import matplotlib.pyplot as plt
import sys
#функция для построения графика. В качестве аргумента передается список слов
def draw_plot(x:list, count=0):
    y = [len(i) for i in x]
    fig = plt.figure(dpi = 150, facecolor='lightgrey')
    ax = plt.axes([0.06, 0.06, 0.9, 0.9], facecolor='#d0feeb')
    ax.grid(color='r', alpha=0.5, ls='--')
    plot_1 = ax.plot(x, y, color='#159eff', marker='o', markerfacecolor='w', lw=3, markeredgecolor='#00FA9A', markeredgewidth=3, alpha=0.6)
    plt.show()


lst_in = list(map(str.strip, sys.stdin.readlines()))#считываем несколько предложений в виде отдельных строк
k = []

for i in lst_in:
    a = list(re.split(r'[.,:;!-?\s]+', i))#превращаем каждое предложение во вложенный список из слов
    k.append(a)
for i in k:
    if len(i[-1]) == 0:
        i.pop(-1)

# for i in k:#общий список вложенных списков(предложений) перебираем циклом и передаем в функцию по отдельности
#     draw_plot(i)


def min_word_len(i): #функция возвращает длину самого короткого слова в списке
    f = []
    for j in i:
        f.append(len(j))
    return min(f)

def list_min_words(i): #функция формирует список из самых коротких слов
    f = []
    for j in i:
       if len(j) == min_word_len(i):
           f.append(j)
    return f

def max_word_len(i):#функция возвращает длину самого длинного слова в списке
    f = []
    for j in i:
        f.append(len(j))
    return max(f)

def list_max_words(i): #функция формирует список из самых длинных слов
    f = []
    for j in i:
       if len(j) == max_word_len(i):
           f.append(j)
    return f

list_short_words = [list_min_words(i) for i in k] #список самых коротких слов из каждого предложения
list_short_words_1 = sum(list_short_words, [])#делаем плоский список, для которого определим длинну каждого слова и поместим на ось Oy
l_tick_short = []
for i in range(len(list_short_words)):
    for j in list_short_words[i]:
        l_tick_short.append(f'{j} - предл.{i}')#делаем плоский список, в котором для каждого слова через дефис указываем номер предложения.
                                                #Затем помещаем полученный список принудительно на ось Ox


list_long_words = [list_max_words(i) for i in k] #список самых длинных слов из каждого предложения
list_long_words_1 = sum(list_long_words, []) #делаем плоский список, для которого определим длинну каждого слова и поместим на ось Oy
l_tick_long = []
for i in range(len(list_long_words)):
    for j in list_long_words[i]:
        l_tick_long.append(f'{j} - предл.{i}')#делаем плоский список, в котором для каждого слова через дефис указываем номер предложения.
                                                #Затем помещаем полученный список принудительно на ось Ox

#рисуем график с самыми короткими словами из всех предложений, по оси Oy длина слова
y = [len(i) for i in list_short_words_1]
fig = plt.figure(dpi = 150, facecolor='lightgrey')
ax = plt.axes([0.06, 0.06, 0.9, 0.9], facecolor='#d0feeb')
ax.grid(color='r', alpha=0.5, ls='--')
ax.set_xticklabels(l_tick_short)
plot_1 = ax.plot(list_short_words_1, y, color='#159eff', marker='o', markerfacecolor='w', lw=3, markeredgecolor='#00FA9A', markeredgewidth=3, alpha=0.6)
plt.show()

#рисуем график с самыми длинными словами из всех предложений, по оси Oy длина слова
y = [len(i) for i in list_long_words_1]
fig = plt.figure(dpi = 150, facecolor='lightgrey')
ax = plt.axes([0.1, 0.3, 0.7, 0.7], facecolor='#d0feeb')
ax.grid(color='r', alpha=0.5, ls='--')
ax.set_xticklabels(l_tick_long, rotation=45, fontsize=7)
plot_1 = ax.plot(list_long_words_1, y, color='#159eff', marker='o', markerfacecolor='w', lw=3, markeredgecolor='#00FA9A', markeredgewidth=3, alpha=0.6)
plt.show()




