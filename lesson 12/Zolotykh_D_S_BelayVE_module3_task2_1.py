import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.gridspec import GridSpec
data = pd.ExcelFile('Population_data.xlsx')
sheet_names = data.sheet_names

df_Europe = pd.read_excel(data, 'Европа')
df_Asia = pd.read_excel(data, 'Азия')
df_Africa = pd.read_excel(data, 'Африка')
df_North_America = pd.read_excel(data, 'Северная Америка')
df_South_America = pd.read_excel(data, 'Южная Америка')
df_Okeania = pd.read_excel(data,'Океания')

#Европа
fig = plt.figure(figsize=(16,9))
gs = GridSpec(nrows=1, ncols=2, figure=fig)
colors = ['b','y','w','r','g']
ax1 = fig.add_subplot(gs[0,0])
a = ax1.bar(df_Europe['Страна'], df_Europe['Население'], width=0.7, color=colors, edgecolor='k')
ax1.set_title('Европа', fontsize=15, color='b')
ax1.set_xlabel('Название стран', fontsize=20, fontstyle = 'italic', color='b')
ax1.set_ylabel('Население', fontsize=20, fontstyle = 'italic', color='b')
ax1.grid(ls='--', color='r', alpha=0.2)
ax1.bar_label(a, padding=5)
ax2 = fig.add_subplot(gs[0,1])
ax2.pie(df_Europe['Население'], labels=df_Europe['Страна'], colors=colors, wedgeprops = {'edgecolor':'k', 'width' :0.6},  shadow=True, explode = [0.1,0.1,0.1,0.1,0.1])
plt.show()

#Азия
fig = plt.figure(figsize=(16,9))
gs = GridSpec(nrows=1, ncols=2, figure=fig)
colors = ['r','green','w','darkgreen','#c00d59']
ax1 = fig.add_subplot(gs[0,0])
a = ax1.bar(df_Asia['Страна'], df_Asia['Население'], width=0.7, color=colors, edgecolor='k')
ax1.set_title('Азия', fontsize=15, color='b')
ax1.set_xlabel('Название стран', fontsize=20, fontstyle = 'italic', color='b')
ax1.set_ylabel('Население', fontsize=20, fontstyle = 'italic', color='b')
ax1.grid(ls='--', color='r', alpha=0.2)
ax1.bar_label(a, padding=5)
ax2 = fig.add_subplot(gs[0,1])
ax2.pie(df_Asia['Население'], labels=df_Asia['Страна'], colors=colors, wedgeprops = {'edgecolor':'k', 'width' :0.6},  shadow=True, explode = [0.1,0.1,0.1,0.1,0.1])
plt.show()

#Африка
fig = plt.figure(figsize=(16,9))
gs = GridSpec(nrows=1, ncols=2, figure=fig)
colors = ['g','y','darkgreen','lightblue','r']
ax1 = fig.add_subplot(gs[0,0])
a = ax1.bar(df_Africa['Страна'], df_Africa['Население'], width=0.7, color=colors, edgecolor='k')
ax1.set_title('Африка', fontsize=15, color='b')
ax1.set_xlabel('Название стран', fontsize=20, fontstyle = 'italic', color='b')
ax1.set_ylabel('Население', fontsize=20, fontstyle = 'italic', color='b')
ax1.grid(ls='--', color='r', alpha=0.2)
ax1.bar_label(a, padding=5)
ax2 = fig.add_subplot(gs[0,1])
ax2.pie(df_Africa['Население'], labels=df_Africa['Страна'], colors=colors, wedgeprops = {'edgecolor':'k', 'width' :0.6},  shadow=True, explode = [0.1,0.1,0.1,0.1,0.1])
plt.show()

#Северная Америка
fig = plt.figure(figsize=(16,9))
gs = GridSpec(nrows=1, ncols=2, figure=fig)
colors = ['b','w','r','lightblue','#f61072']
ax1 = fig.add_subplot(gs[0,0])
a = ax1.bar(df_North_America['Страна'], df_North_America['Население'], width=0.7, color=colors, edgecolor='k')
ax1.set_title('Северная Америка', fontsize=15, color='b')
ax1.set_xlabel('Название стран', fontsize=20, fontstyle = 'italic', color='b')
ax1.set_ylabel('Население', fontsize=20, fontstyle = 'italic', color='b')
ax1.grid(ls='--', color='r', alpha=0.2)
ax1.bar_label(a, padding=5)
ax2 = fig.add_subplot(gs[0,1])
ax2.pie(df_North_America['Население'], labels=df_North_America['Страна'], colors=colors, wedgeprops = {'edgecolor':'k', 'width' :0.6},  shadow=True, explode = [0.1,0.1,0.1,0.1,0.1])
plt.show()

#Южная Америка
fig = plt.figure(figsize=(16,9))
gs = GridSpec(nrows=1, ncols=2, figure=fig)
colors = ['g','y','lightblue','r','darkblue']
ax1 = fig.add_subplot(gs[0,0])
a = ax1.bar(df_South_America['Страна'], df_South_America['Население'], width=0.7, color=colors, edgecolor='k')
ax1.set_title('Южная Америка', fontsize=15, color='b')
ax1.set_xlabel('Название стран', fontsize=20, fontstyle = 'italic', color='b')
ax1.set_ylabel('Население', fontsize=20, fontstyle = 'italic', color='b')
ax1.grid(ls='--', color='r', alpha=0.2)
ax1.bar_label(a, padding=5)
ax2 = fig.add_subplot(gs[0,1])
ax2.pie(df_South_America['Население'], labels=df_South_America['Страна'], colors=colors, wedgeprops = {'edgecolor':'k', 'width' :0.6},  shadow=True, explode = [0.1,0.1,0.1,0.1,0.1])
plt.show()

#Океания
fig = plt.figure(figsize=(18,9))
gs = GridSpec(nrows=1, ncols=2, figure=fig)
colors = ['darkblue','k','w','lightblue','g']
ax1 = fig.add_subplot(gs[0,0])
a = ax1.bar(df_Okeania['Страна'], df_Okeania['Население'], width=0.7, color=colors, edgecolor='k')
ax1.tick_params(axis='x',labelrotation=10)
ax1.set_title('Океания', fontsize=15, color='b')
ax1.set_xlabel('Название стран', fontsize=20, fontstyle = 'italic', color='b')
ax1.set_ylabel('Население', fontsize=20, fontstyle = 'italic', color='b')
ax1.grid(ls='--', color='r', alpha=0.2)
ax1.bar_label(a, padding=5)
ax2 = fig.add_subplot(gs[0,1])
ax2.pie(df_Okeania['Население'], labels=df_Okeania['Страна'], colors=colors, wedgeprops = {'edgecolor':'k', 'width' :0.6},  shadow=True, explode = [0.1,0.1,0.1,0.1,0.1])
plt.show()