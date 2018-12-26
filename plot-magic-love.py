# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 19:09:28 2018

@author: xing.wu
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


fig = plt.figure(figsize=(8, 6))
ax = plt.axes(xlim = (-3, 3), ylim = (-2.8, 3.2))

line, = ax.plot([], [], '#FF69B4', lw=2)
# #FF69B4叫做 Hotpink

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(-3, 3, 1000)
    
    y = (np.abs(x)**(2/3)) + 0.9*((3.3 - (x**2))**(1/2)) * np.sin(i * np.pi * x)
    
    line.set_data(x, y)
    
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)
# 必须要存 html，不能存 mp4

anim.save('basic_animation.html', fps=30, extra_args=['-vcodec', 'libx264'])
plt.show()


import argparse
# 创建解析步骤
parser = argparse.ArgumentParser(description='Process some integers.')

# 添加参数步骤
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers')
# 解析参数步骤  
args = parser.parse_args()
print(args.accumulate(args.integers))
