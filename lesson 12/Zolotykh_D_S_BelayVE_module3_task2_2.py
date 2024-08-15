import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.gridspec import GridSpec
#функция построания диаграмм
def draw_plot_and_bar(colors_for_country:list, label:list, countries:list, population:list):
    fig = plt.figure(figsize=(18, 9))
    gs = GridSpec(nrows=1, ncols=2, figure=fig)
    colors = colors_for_country
    ax1 = fig.add_subplot(gs[0, 0])
    a = ax1.bar(countries, population, width=0.7, color=colors, edgecolor='k')
    ax1.tick_params(axis='x', labelrotation=10)
    ax1.set_title(label, fontsize=15, color='b')
    ax1.set_xlabel('Название стран', fontsize=20, fontstyle='italic', color='b')
    ax1.set_ylabel('Население', fontsize=20, fontstyle='italic', color='b')
    ax1.grid(ls='--', color='r', alpha=0.2)
    ax1.bar_label(a, padding=5)
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.pie(population, labels=population, colors=colors,
            wedgeprops={'edgecolor': 'k', 'width': 0.6}, shadow=True, explode=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
    ax2.legend(countries, loc='center')
    plt.show()


#импорт данных из файла xlsx
#учитываем, что в исходном файле xlsx в каждой таблице население и страны уже отсортирвоаны от большего к меньшему по параметру населения,
# то есть нужен первый элемент
data = pd.ExcelFile('Data - Zolotykh_D_S_BelayVE_module3_task2_1.xlsx')
sheet_names = data.sheet_names
population = []
country = []
for i in sheet_names:
    lst = pd.read_excel(data, sheet_name=i)
    population.append(list(lst['Население'])[0])#получаем данные по численности наиболее населенных стран
    country.append(list(lst['Страна'])[0])#полуаем список наиболее населенных стран

#подготоваливаем данные для построания диаграмм
colors_for_countries = ['royalblue', 'r', 'g', 'w', 'y','darkblue']
label = 'Наиболее населенные страны регионов'

draw_plot_and_bar(colors_for_country=colors_for_countries, label=label, countries=country, population=population)
