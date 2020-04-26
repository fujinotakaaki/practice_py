# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
# 補助線の描画

# 0-1の乱数を100個生成
x = np.linspace(.7, 30., 100)
y = np.log(x)/x

plt.axvline(x=np.e)
for i in range(2):
    plt.axhline(y=i * np.e**(-1))
plt.plot(x,y)
plt.show()
