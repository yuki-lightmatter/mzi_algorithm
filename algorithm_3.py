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

ax.set_title('MZI Rock Algorithm 3')
ax.set_xlabel('DAC Code [LSB]')
ax.set_ylabel('ADC Code [LSB]')
yaxis_label = ['','CODE-4','CODE-3','CODE-2','CODE-1','CODE','CODE+1','CODE+2','CODE+3','CODE+4','CODE+5','CODE+6']
xaxis_label = ['CODE\n-5x Step','CODE\n-4x Step','CODE\n-3x Step','CODE\n-2x Step','CODE\n-1x Step','CODE','CODE\n+1x Step','CODE\n+2x Step','CODE\n+3x Step','CODE\n+4x Step','CODE\n+5x Step','CODE\n+6x Step']
ax.set_xlim([-3, 3])
ax.set_xticks(xaxis)
ax.set_xticklabels(xaxis_label,ha = 'center', fontsize = 9)
ax.set_ylim([-3, 3])
ax.set_yticks(xaxis)
ax.set_yticklabels(yaxis_label)
ax.grid(True, which="both")

base_code = [2,2,3,3,4,4,3,1,-1,-1,-2,-5]
move_points = [[4,'T0 1st','','-1'],
               [5,'T0 2nd','slope_try = -1\nset slope = -1 and Reduce DAC Code','-1'],
               [3,'T1 1st','','-1'],
               [4,'T1 2nd','slope_try = 0\nUse slope (-1) for decision and Reduce DAC Code','-1'],
               [2,'T2 1st','','-1'],
               [3,'T2 2nd','slope_try = -1\nset slope = -1 and Reduce DAC Code','-1'],
               [1,'T3 1st','','-1'],
               [2,'T3 2nd','slope_try = -1\nset slope = -1 and Reduce DAC Code','-1'],
               [0,'T4 1st','','-1'],
               [1,'T4 2nd','slope_try = -1\nset slope = -1 and Reduce DAC Code','-1'],
               [-1,'T5 1st','','-1'],
               [0,'T5 2nd','slope_try = 0\nUse slope (-1) for decision and Reduce DAC Code','-1'],
               [-2,'T6 1st','','-1'],
               [-1,'T6 2nd','slope_try = 1\nset slope = 1 and Increase DAC Code','1'],
               [-1,'T7 1st','','1'],
               [0,'T7 2nd','slope_try = 0\nUse slope (1) for decision and Increase DAC Code','1'],
               [0,'T8 1st','','1'],
               [1,'T8 2nd','slope_try = -1\nset slope = -1 and Reduce DAC Code','-1'],
               [-1,'T9 1st','','-1'],
               [0,'T9 2nd','slope_try = 0\nUse slope (-1) for decision and Reduce DAC Code','-1'],
               [-2,'T10 1st','','-1'],
               [-1,'T10 2nd','slope_try = 1\nset slope = 1 and Increase DAC Code','1'],
               [-1,'T11 1st','','1'],
               [0,'T11 2nd','slope_try = 0\nUse slope (1) for decision and Increase DAC Code','1'],
               [0,'T12 1st','','1'],
               [1,'T12 2nd','slope_try = -1\nset slope = -1 and Reduce DAC Code','-1'],               
              ]
text_offset = 0.1

color_switch = (lambda i: colors[4] if i % 2 else colors[3])

ims = []
for i in range(len(move_points)):
    im_b = ax.plot(xaxis,base_code, color = colors[1],markersize = 15,linestyle="-", alpha = 0.5)
    im_p = ax.plot(move_points[i][0],base_code[move_points[i][0] - xaxis[0]], color = color_switch(i),marker = '.', markersize = 15,linestyle="")
    im_t = ax.text(move_points[i][0] + text_offset,base_code[move_points[i][0] - xaxis[0]]  + text_offset, move_points[i][1],color = color_switch(i))
    im_t1 = ax.text(-1, -2, move_points[i][2], weight='bold', fontsize = 16,color = colors[0],backgroundcolor = 'white',va = 'center',ha = 'center')
    im_t2 = ax.text(4, 5, f'Trial = {int(i/2)}\nSlope = {move_points[i][3]}',fontsize = 14,color = 'black',backgroundcolor = 'white',va = 'center',ha = 'center')
    ims.append(im_b + im_p + [im_t] + [im_t1] + [im_t2])
ani = animation(fig, ims,interval=1700)
ani.save("sample.gif", writer="pillow")
plt.close()
from IPython.display import Image
Image(filename='./sample.gif')