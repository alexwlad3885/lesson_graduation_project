import dp_оne_dimensional_data as dp_1
import dp_two_dimensional_data as dp_2
import dp_three_dimensional_data as dp_3


if __name__ == '__main__':
    dp_1.fig, dp_1.axes = dp_1.plt.subplots(1, 3)
    dp_1.fig.set_size_inches(10.5, 6)
    dp_1.fig.set_tight_layout(True)
    dp_1.fig.show()

    dp_2.fig, dp_2.axes = dp_2.plt.subplots(1, 3)
    dp_2.fig.set_size_inches(10.5, 6)
    dp_2.fig.set_tight_layout(True)
    dp_2.fig.text(0.16, 0.73, 'г. Владимир\nданные по ковиду\nза 2020 г.', fontsize=10, style='italic', bbox={
                  'facecolor': '#ff7f0e', 'alpha': 0.5, 'pad': 10}, ha='center', va='center')
    dp_2.fig.text(0.495, 0.73, 'г. Владимир\nданные по ковиду\nза 2020 г.', fontsize=10, style='italic', bbox={
                  'facecolor': '#9467bd', 'alpha': 0.5, 'pad': 10}, ha='center', va='center')
    dp_2.fig.show()

    dp_3.fig_1 = dp_3.plt.figure(figsize=(12, 8))
    dp_3.ax_1 = dp_3.fig_1.add_subplot(projection='3d')
    dp_3.fig_1.show()
    dp_3.fig_2 = dp_3.plt.figure(figsize=(12, 8))
    dp_3.ax_2 = dp_3.fig_2.add_subplot(projection='3d')
    dp_3.fig_2.show()
    dp_3.fig_3.show()
    dp_3.fig_4, dp_3.ax_4 = dp_3.plt.subplots()
    dp_3.fig_4.set_size_inches(10.5, 6)
    dp_3.fig_4.show()

"""
import tkinter as tk
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import dp_оne_dimensional_data as dp_1


df = pd.read_csv('train.csv', usecols=['Sex'])
count_sex = df.groupby(['Sex'])['Sex'].count()
sex = ['женщины', 'мужчины']

window = tk.Tk()
window.title('Графики')
window.geometry("500x500")
window.resizable(False, False)
fig, axes = plt.subplots(3, 4)
fig.set_size_inches(10.5, 6)
fig.show()
# fig = Figure()

# plot_1 = dp_1.matplotlib_one(count_sex, sex)

axes[0].pie(count_sex.values, labels=sex, explode=(0.1, 0.0), autopct='%1.2f%%')


plt.show()



plot1 = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()

# размещение холста в окне Tkinter
canvas.get_tk_widget().pack()

# создание панели инструментов Matplotlib
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()

# размещение панели инструментов в окне Tkinter
canvas.get_tk_widget().pack()

# def plot():
#     # the figure that will contain the plot
#     fig = Figure(figsize=(5, 5),
#                  dpi=100)
#
#     # list of squares
#     y = [i ** 2 for i in range(101)]
#
#     # adding the subplot
#     plot1 = fig.add_subplot(111)
#
#     # plotting the graph
#     plot1.plot(y)
#
#     # creating the Tkinter canvas
#     # containing the Matplotlib figure
#     canvas = FigureCanvasTkAgg(fig,
#                                master=window)
#     canvas.draw()
#
#     # placing the canvas on the Tkinter window
#     canvas.get_tk_widget().pack()
#
#     # creating the Matplotlib toolbar
#     toolbar = NavigationToolbar2Tk(canvas,
#                                    window)
#     toolbar.update()
#
#     # placing the toolbar on the Tkinter window
#     canvas.get_tk_widget().pack()


# The main tkinter window

# кнопка, которая отображала бы график
plot_button = tk.Button(master=window,
                        command=plot_1,
                        height=2,
                        width=10,
                        text="Plot")
plot_button.pack()


window.mainloop()
"""
