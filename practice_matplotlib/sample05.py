# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
# ヒストグラム作成、描画

# 0-1の乱数を100個生成
x = np.random.rand(100)

# データを２０の階級に分割
plt.hist(x, 20)
plt.show()
