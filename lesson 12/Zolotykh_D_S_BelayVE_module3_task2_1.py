import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.gridspec import GridSpec
#импорт данных из файла xlsx
data = pd.ExcelFile('Data - Zolotykh_D_S_BelayVE_module3_task2_1.xlsx')
sheet_names = data.sheet_names
#подготовка отдельных дейтафреймов по листам книги Excel
df_Europe = pd.read_excel(data, 'Европа')
df_Asia = pd.read_excel(data, 'Азия')
df_Africa = pd.read_excel(data, 'Африка')
df_North_America = pd.read_excel(data, 'Северная Америка')
df_South_America = pd.read_excel(data, 'Южная Америка')
df_Okeania = pd.read_excel(data,'Океания')
#функция для построения двух типов графиков и размещения их на одной плоскости
def draw_plot_and_bar(colors_for_country:list, label, data_frame):
    fig = plt.figure(figsize=(18, 9))
    gs = GridSpec(nrows=1, ncols=2, figure=fig)
    colors = colors_for_country
    ax1 = fig.add_subplot(gs[0, 0])
    a = ax1.bar(data_frame['Страна'], data_frame['Население'], width=0.7, color=colors, edgecolor='k')
    ax1.tick_params(axis='x', labelrotation=10)
    ax1.set_title(label, fontsize=15, color='b')
    ax1.set_xlabel('Название стран', fontsize=20, fontstyle='italic', color='b')
    ax1.set_ylabel('Население', fontsize=20, fontstyle='italic', color='b')
    ax1.grid(ls='--', color='r', alpha=0.2)
    ax1.bar_label(a, padding=5)
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.pie(data_frame['Население'], labels=data_frame['Население'], colors=colors,
            wedgeprops={'edgecolor': 'k', 'width': 0.6}, shadow=True, explode=[0.1, 0.1, 0.1, 0.1, 0.1])
    ax2.legend(data_frame['Страна'], loc='center')
    plt.show()
#готовим данные для построения графиков
colors_for_Europe = ['b','y','w','r','g']
colors_for_Asia = ['r','green','w','darkgreen','#c00d59']
colors_for_Africa = ['g','y','darkgreen','lightblue','r']
colors_for_Northen_America = ['b','w','r','lightblue','#f61072']
colors_for_South_America = ['g','y','lightblue','r','darkblue']
colors_for_Oceania = ['darkblue','k','w','lightblue','g']

label_for_Europe = 'Европа'
label_for_Asia = 'Азия'
label_for_Africa = 'Африка'
label_for_Northen_America = 'Северная Америка'
label_for_South_America = 'Южная Америка'
label_for_Oceania='Океания'
#запускаем функцию построения
draw_plot_and_bar(colors_for_Europe, label_for_Europe, data_frame=df_Europe)
draw_plot_and_bar(colors_for_Asia, label_for_Asia, data_frame=df_Asia)
draw_plot_and_bar(colors_for_Africa, label_for_Africa, data_frame=df_Africa)
draw_plot_and_bar(colors_for_Northen_America, label_for_Northen_America, data_frame=df_North_America)
draw_plot_and_bar(colors_for_South_America,label_for_South_America,data_frame=df_South_America)
draw_plot_and_bar(colors_for_Oceania, label_for_Oceania, data_frame=df_Okeania)
