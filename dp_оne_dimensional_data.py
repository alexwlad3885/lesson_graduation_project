from matplotlib import pyplot as plt
import pandas as pd
from datetime import datetime
import seaborn as sns
import plotly.express as px


df = pd.read_csv('train.csv', usecols=['Sex'])
count_sex = df.groupby(['Sex'])['Sex'].count()


fig, axes = plt.subplots(1, 3)
fig.set_size_inches(10.5, 6)
fig.set_tight_layout(True)
fig.show()
sex = ['женщины', 'мужчины']
# график построен с помощью библиотеки Matplotlib

time_start_1 = datetime.now()

axes[0].pie(count_sex.values, labels=sex, explode=(0.1, 0.0), autopct='%1.2f%%')
axes[0].set(title='график построен\n'
                  'с помощью библиотеки\n'
                  ' Matplotlib\n')

time_end_1 = datetime.now()
time_res_1 = time_end_1 - time_start_1
td_1 = pd.Timedelta(time_res_1)

# график построен с помощью библиотеки Seaborn

time_start_2 = datetime.now()

palette_color = sns.color_palette('pastel')
axes[1].pie(count_sex, labels=sex, colors=palette_color, explode=(0.1, 0.0), autopct='%1.2f%%')
axes[1].set(title='график построен\n'
                  'с помощью библиотеки\n'
                  ' Seaborn\n')

time_end_2 = datetime.now()
time_res_2 = time_end_2 - time_start_2
td_2 = pd.Timedelta(time_res_2)

# график построен с помощью библиотеки Plotly

time_start_3 = datetime.now()

fig_ = px.pie(count_sex,
              values=count_sex,
              names=sex,
              title='график построен\n'
                    'с помощью библиотеки\n'
                    'Plotly\n',
              labels={'female': 'женщины', 'male': 'мужчины'},
              width=400, height=400)
fig_.update_layout(title={
        "y": 1,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top"
    }
)
fig_.update_traces(textposition='inside',
                   textinfo='percent+label',
                   sort=False)
fig_.show()

time_end_3 = datetime.now()
time_res_3 = time_end_3 - time_start_3
td_3 = pd.Timedelta(time_res_3)

time_res = [td_1.microseconds, td_2.microseconds, td_3.microseconds]

# анализ быстродействия построения графиков

libr = ['Matplotlib', 'Seaborn', 'Plotly']
axes[2].bar(libr, time_res, width=0.6, edgecolor="white", linewidth=0.7)
for i in range(len(libr)):
    axes[2].text(i, time_res[i], time_res[i], ha='center',
                 bbox=dict(facecolor='red', alpha=.8))
axes[2].set(title='сравнение\n'
                  'времени построения\n'
                  'графиков 1D с помощью\n'
                  'разных библиотек\n',
            yticklabels=[]
            )
axes[2].set_xticks(libr)
axes[2].set_xticklabels(labels=libr, rotation=45)
axes[2].set_ylabel('')
axes[2].autoscale()

plt.show()
