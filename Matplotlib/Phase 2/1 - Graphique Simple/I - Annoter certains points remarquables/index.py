# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 21:34:54 2022

@author: Muriel
"""
from pylab import *

figure(figsize=(8, 5), dpi= 80)
subplot(111)

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plot(X, C, color="green", linewidth=2.5, linestyle="-", label="Cosinus")
plot(X, S, color="red", linewidth=2.5, linestyle="-", label="Sinus")

ax= gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

xlim(X.min()*1.1, X.max()*1.1)
xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

ylim(C.min()*1.1, C.max()*1.1)
yticks([-1, +1], [r'$-1$', r'$+1$'])

legend(loc='upper left')

t = 2- 
#savefig("image.png", dpi=72)

show()