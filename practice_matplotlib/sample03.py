# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
# 棒グラフの描画

t = np.pi
# 三角関数のグラフ
x = np.linspace( -t/6, 2*t, 100)

y = np.sin(x)
plt.plot(x,y,label="line", alpha=0.6, color="#888888", linewidth=3) # => 正弦関数プロット
plt.bar(x,y, label='bar') # => 棒グラフ

plt.title("trigonometric function") # => グラフタイトル
plt.xlabel("rad") # => x軸ラベル
plt.ylabel("sin") # => y軸ラベル
plt.legend() # => 凡例表示フラグ


plt.show() # グラフ描画
