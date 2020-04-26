# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
# グラフに領域の描画


x = np.linspace(-1, 2.5, 100)
y = x*(x-1)*(x-2)/10

plt.plot(x,y)
plt.axhline(y=0) # y=0
plt.axvspan(-1,0,alpha=.25) # -1<=x<=0
plt.axvspan(1,2,alpha=.25) # 1<=x<=2.5
plt.axhspan(-1,0,alpha=.25) # -1<=y<=0
plt.show()
