# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
# グラフ描画（オプション利用）

t = np.pi
# 三角関数のグラフ
x = np.linspace( -t/6, 2*t, 100)

y1 = np.sin(x)
plt.plot(x,y1,label="sin", alpha=0.6, color="#888888", linewidth=3) # => 正弦関数プロット

y2 = np.cos(x)
plt.plot(x,y2,label="cos", color="red") # => 余弦関数プロット

y3 = 1/(1+x**2)

# y3 = np.tan(x)
# plt.plot(x,y3,label="tan") # => 正接関数プロット
plt.plot(x,y3,label="test", color="forestgreen", linestyle=":", linewidth=2)

plt.title("trigonometric function") # => グラフタイトル
plt.xlabel("rad") # => x軸ラベル
plt.ylabel("result") # => y軸ラベル
plt.legend() # => 凡例表示フラグ


plt.show() # グラフ描画
