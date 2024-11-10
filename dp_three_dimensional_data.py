from matplotlib import pyplot as plt
import pandas as pd
from datetime import datetime
import seaborn as sns
import plotly.graph_objects as go
import numpy as np
from matplotlib import cm
import matplotlib.colors as col
import functions as fnc


months = fnc.data_reductions('covid.csv')['months']
heading = fnc.data_reductions('covid.csv')['heading']
sick = fnc.data_reductions('covid.csv')['sick']
locality_sick = fnc.data_reductions('covid.csv')['locality_sick']
locality = fnc.data_reductions('covid.csv')['locality']
month_list = fnc.month_conversion(months)
a = []
for i in range(len(locality_sick)):
    a.append(locality_sick[i])
mas = np.array(a)

# график построен с помощью библиотеки Matplotlib
time_start_1 = datetime.now()

fig_1 = plt.figure(figsize=(12, 8))
ax_1 = fig_1.add_subplot(projection='3d')

y = len(locality)
cmap = cm.ScalarMappable(col.Normalize(0, y), 'plasma')
for ind, row in enumerate(mas):
    ax_1.bar(month_list, row, zs=ind, zdir='y', width=0.6, bottom=0, alpha=0.8, color=cmap.to_rgba(ind))
ax_1.set_xlabel('')
ax_1.set_ylabel('город')
ax_1.set_zlabel('заболевшие')
ax_1.set_title('График построен с помощью библиотеки Matplotlib', loc='center', fontsize=14)
fig_1.legend(labels=locality, loc='center left')


time_end_1 = datetime.now()
time_res_1 = time_end_1 - time_start_1
td_1 = pd.Timedelta(time_res_1)

fig_1.show()

# график построен с помощью библиотеки Seaborn
time_start_2 = datetime.now()

fig_2 = plt.figure(figsize=(12, 8))
ax_2 = fig_2.add_subplot(projection='3d')

y = len(locality)
palette_color = sns.color_palette('pastel', y)
for i, row in enumerate(mas):
    ax_2.bar(month_list, row, zs=i, zdir='y', width=0.6, bottom=0, alpha=0.8, color=np.array(palette_color[i]))
ax_2.set_xlabel('')
ax_2.set_ylabel('город')
ax_2.set_zlabel('заболевшие')
ax_2.set_title('График построен с помощью библиотеки Seaborn', loc='center', fontsize=14)
fig_2.legend(labels=locality, loc='center left')

time_end_2 = datetime.now()
time_res_2 = time_end_2 - time_start_2
td_2 = pd.Timedelta(time_res_2)

fig_2.show()
# график построен с помощью библиотеки Plotly

time_start_3 = datetime.now()

z = mas
sh_0, sh_1 = z.shape
x, y = np.linspace(0, sh_0, sh_0), np.linspace(0, sh_1, sh_1)
layout = go.Layout(showlegend=True)


fig_3 = go.Figure(data=[go.Surface(z=z, x=x, y=y)], layout=layout)
fig_3.update_layout(title='график построен\n'
                    'с помощью библиотеки\n'
                    'Plotly\n',
                    scene=dict(
                            xaxis_title='месяцы',
                            yaxis_title='города',
                            zaxis_title='количество заболевших'),
                    legend_orientation="h",
                    autosize=False,
                    width=800, height=800,
                    margin=dict(l=65, r=50, b=65, t=90))
fig_3.update_layout(title={'y': 0.85, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'})


time_end_3 = datetime.now()
time_res_3 = time_end_3 - time_start_3
td_3 = pd.Timedelta(time_res_3)

fig_3.show()
# анализ быстродействия построения графиков
fig_4, ax_4 = plt.subplots()
fig_4.set_size_inches(10.5, 6)
time_res = [td_1.microseconds, td_2.microseconds, td_3.microseconds]
libr = ['Matplotlib', 'Seaborn', 'Plotly']
ax_4.bar(libr, time_res, width=0.6, edgecolor="white", linewidth=0.7)
for i in range(len(libr)):
    ax_4.text(i, time_res[i], str(time_res[i]), ha='center',
              bbox=dict(facecolor='red', alpha=.8))
ax_4.set(title='сравнение времени построения графиков 3D с помощью разных библиотек',
         yticklabels=[])
ax_4.set_xticklabels(libr, rotation=45)
ax_4.set_ylabel('')
ax_4.autoscale()


fig_4.show()
plt.show()
