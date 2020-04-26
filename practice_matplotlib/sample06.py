# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
# 複数のヒストグラム作成、描画

# 0-1の乱数を100個生成
x1 = np.random.rand(100)
# 0-1の乱数を100個生成し、それぞれの自乗をとる
x2 = np.random.rand(100)**2

# データを２０の階級に分割
# ２データ分入力
plt.hist([x1, x2], 20, stacked=True)
plt.show()
