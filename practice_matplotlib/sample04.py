# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
# 円グラフの描画

x = [40, 25, 20, 10, 3, 2]
arr = [ "a", "b", "c", "d", "e", "f"]


# 円グラフ用データ入力
plt.pie(x, labels=arr, shadow=True, autopct='%1.f%%',startangle=90)
plt.legend()
plt.show()
