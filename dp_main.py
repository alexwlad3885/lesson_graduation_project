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
