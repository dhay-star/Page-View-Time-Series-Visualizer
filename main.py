# main.py

import matplotlib.pyplot as plt
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

# work 3 Function 

print("Generating line plot : ")
fig1 = draw_line_plot()
plt.show()

print("Generating bar plot : ")
fig2 = draw_bar_plot()
plt.show()

print("Generating box plots : ")
fig3 = draw_box_plot()
plt.show()
