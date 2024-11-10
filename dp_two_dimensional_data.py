from matplotlib import pyplot as plt
import pandas as pd
from datetime import datetime
import seaborn as sns
import plotly.express as px
import functions as fnc


months = fnc.data_reductions('covid.csv')['months']
del months[0]
month = fnc.month_conversion(months)
month = month[0: 8]
locality_sick = fnc.data_reductions('covid.csv')['locality_sick']
sick = fnc.data_reductions('covid.csv')['locality_sick'][0][0:8]


fig, axes = plt.subplots(1, 3)
fig.set_size_inches(10.5, 6)
fig.set_tight_layout(True)
fig.text(0.16, 0.73, 'г. Владимир\nданные по ковиду\nза 2020 г.', fontsize=10, style='italic', bbox={
            'facecolor': '#ff7f0e', 'alpha': 0.5, 'pad': 10}, ha='center', va='center')
fig.text(0.495, 0.73, 'г. Владимир\nданные по ковиду\nза 2020 г.', fontsize=10, style='italic', bbox={
            'facecolor': '#9467bd', 'alpha': 0.5, 'pad': 10}, ha='center', va='center')
fig.show()


# график построен с помощью библиотеки Matplotlib
time_start_1 = datetime.now()

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']

axes[0].bar(month, sick, width=0.6, edgecolor="white", linewidth=0.7, color=colors, alpha=0.5)
for i in range(len(month)):
    axes[0].text(i, sick[i], sick[i], ha='center',
                 bbox=dict(facecolor='red', alpha=.8))

axes[0].set(title='график построен\n'
                  'с помощью библиотеки\n'
                  ' Matplotlib\n')
axes[0].set_xticks(month)
axes[0].set_xticklabels(labels=month, rotation=45)
axes[0].set_ylabel('')
axes[0].autoscale()

time_end_1 = datetime.now()
time_res_1 = time_end_1 - time_start_1
td_1 = pd.Timedelta(time_res_1)

# график построен с помощью библиотеки Seaborn

time_start_2 = datetime.now()

palette_color = sns.color_palette('pastel', n_colors=8, as_cmap=True)
sns.barplot(x=month, y=sick, ax=axes[1], palette=palette_color)
for i in axes[1].containers:
    axes[1].bar_label(i, padding=-25, rotation=90, label_type='edge', fontweight='bold')
axes[1].set_xticks(month)
axes[1].set_xticklabels(labels=month, rotation=45)
axes[1].set(title='график построен\n'
                  'с помощью библиотеки\n'
                  ' Seaborn\n')
time_end_2 = datetime.now()
time_res_2 = time_end_2 - time_start_2
td_2 = pd.Timedelta(time_res_2)

# график построен с помощью библиотеки Plotly

time_start_3 = datetime.now()

fig_p = px.bar(sick, x=month, y=sick,
               color=month,
               labels={'x': 'месяцы 2020 г.', 'y': 'количество заболевших'},
               title='график построен\n'
                     'с помощью библиотеки\n'
                     'Plotly\n',
               width=800, height=400)
fig_p.update_layout(
    title={'y': 0.85, 'x': 0.5, 'xanchor': 'center', 'yanchor': 'top'},
    legend={'title': 'месяцы'}
)

fig_p.show()

time_end_3 = datetime.now()
time_res_3 = time_end_3 - time_start_3
td_3 = pd.Timedelta(time_res_3)

# анализ быстродействия построения графиков
time_res = [td_1.microseconds, td_2.microseconds, td_3.microseconds]
libr = ['Matplotlib', 'Seaborn', 'Plotly']
axes[2].bar(libr, time_res, width=0.6, edgecolor="white", linewidth=0.7)
for i in range(len(libr)):
    axes[2].text(i, time_res[i], time_res[i], ha='center',
                 bbox=dict(facecolor='red', alpha=.8))
axes[2].set(title='сравнение\n'
                  'времени построения\n'
                  'графиков 2D с помощью\n'
                  'разных библиотек\n',
            yticklabels=[]
            )
axes[2].set_xticks(libr)
axes[2].set_xticklabels(labels=libr, rotation=45)
axes[2].set_ylabel('')
axes[2].autoscale()

fig.show()
plt.show()
