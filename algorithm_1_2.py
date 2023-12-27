import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation as animation
from matplotlib import cm
import numpy as np
from IPython.display import HTML
plot_parameters = {'font.family' : 'serif',
                   'font.serif' : 'Times New Roman',
                   'axes.labelsize': 12,
                   'axes.titlesize': 14,
                   'font.size': 10}
plt.rcParams.update(plot_parameters)
colors = cm.Set1.colors

fig, ax = plt.subplots(figsize=(10,6))
# x-axis range setting
xaxis = np.arange(-5,7,1)

ax.set_title('MZI Rock Algorithm 1 and 2')
ax.set_xlabel('DAC Code [LSB]')
ax.set_ylabel('ADC Code [LSB]')
yaxis_label = ['','CODE-4','CODE-3','CODE-2','CODE-1','CODE','CODE+1','CODE+2','CODE+3','CODE+4','CODE+5','CODE+6']
xaxis_label = ['CODE\n-5x Step','CODE\n-4x Step','CODE\n-3x Step','CODE\n-2x Step','CODE\n-1x Step','CODE','CODE\n+1x Step','CODE\n+2x Step','CODE\n+3x Step','CODE\n+4x Step','CODE\n+5x Ste5','CODE\n+6x Step']
ax.set_xlim([-3, 3])
ax.set_xticks(xaxis)
ax.set_xticklabels(xaxis_label,ha = 'center', fontsize = 9)
ax.set_ylim([-3, 3])
ax.set_yticks(xaxis)
ax.set_yticklabels(yaxis_label)
ax.grid(True, which="both")

base_code = [2,2,3,3,4,4,3,1,-1,-1,-2,-5]
move_points = [[5,'T0 1st',''],
               [6,'T0 2nd','Slope = -1\nReduce DAC Code'],
               [4,'T1 1st',''],
               [5,'T1 2nd','Slope = -1\nReduce DAC Code'],
               [3,'T2 1st',''],
               [4,'T2 2nd','Slope = 0\nLocked'],
               [3,'T3 1st',''],
               [4,'T3 2nd','Slope = 0\nLocked'],
               [3,'T4 1st',''],
               [4,'T4 2nd','Slope = 0\nLocked'],
               [3,'T5 1st',''],
               [4,'T5 2nd','Slope = 0\nLocked'],
              ]
text_offset = 0.1

color_switch = (lambda i: colors[4] if i % 2 else colors[3])

ims = []
for i in range(len(move_points)):
    im_b = ax.plot(xaxis,base_code, color = colors[1],markersize = 15,linestyle="-", alpha = 0.5)
    im_p = ax.plot(move_points[i][0],base_code[move_points[i][0] - xaxis[0]], color = color_switch(i),marker = '.', markersize = 15,linestyle="")
    im_t = ax.text(move_points[i][0] + text_offset,base_code[move_points[i][0] - xaxis[0]]  + text_offset, move_points[i][1],color = color_switch(i))
    # im_t1 = ax.text(3, 4, move_points[i][2],fontsize = 14,color = colors[1],backgroundcolor = 'white',ha = 'center')
    im_t1 = ax.text(-1, -2, move_points[i][2], weight='bold', fontsize = 16,color = colors[0],backgroundcolor = 'white',va = 'center',ha = 'center')
    im_t2 = ax.text(4, 5, f'Trial = {int(i/2)}',fontsize = 14,color = 'black',backgroundcolor = 'white',va = 'center',ha = 'center')
    ims.append(im_b + im_p + [im_t] + [im_t1] + [im_t2])
ani = animation(fig, ims,interval=1700, repeat=False)
ani.save("sample.gif", writer="pillow")
plt.close()
from IPython.display import Image
Image(filename='./sample.gif')
