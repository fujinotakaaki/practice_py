# coding:utf-8
import math
import numpy as np

### リストとndarrayのちがい
arr1 = range(10,50,10)
arr2 = np.array(range(10,50,10))

# そのまま出力
print arr1 #=> [10, 20, 30, 40]
print arr2 # => [10 20 30 40]


# 後ろからスカラー倍
print arr1*2 # => [10, 20, 30, 40, 10, 20, 30, 40]
print arr2*2 # => [20 40 60 80]

# 前からスカラー倍
print 2*arr1 # => [10, 20, 30, 40, 10, 20, 30, 40]
print 2*arr2 # => [20 40 60 80]

# 行列積
#print(arr1 * arr1) # => TypeError
print(arr2 * arr2) # => [100 400 900 1600] 数学の行列の計算法とは異なる

# リストとndarrayの四則演算
print(arr1 + arr2) # => [20 40 60 80]
print(arr1 - arr2) # => [0 0 0 0]
print(arr1 * arr2) # => [100 400 900 1600] 数学の行列の計算法とは異なる
print(arr1 / arr2) # => [1 1 1 1] 数学の行列の計算法とは異なる

arr3 = np.array(range(1,9))
print arr3 # => [1 2 3 4 5 6 7 8]

# 要素数が異なる場合の挙動(参考書は掛け算はいけるって書いてあったけど条件がちがうのかな)
#print(arr2 + arr3) # => ValueError
#print(arr2 - arr3) # => ValueError
#print(arr2 * arr3) # => ValueError
#print(arr2 / arr3) # => ValueError


#print(arr3 + arr2) # => ValueError
#print(arr3 - arr2) # => ValueError
#print(arr3 * arr2) # => ValueError
#print(arr3 / arr2) # => ValueError

# 特殊なndarrayの生成
print np.zeros(4) # => [0.  0.  0.  0.]
print np.ones(5) # => [1.  1.  1.  1.  1.]

# listとndarrayの要素のクラス
print 3.14.__class__.__name__ # => float
print math.pi.__class__.__name__ # => float
print arr1[0].__class__.__name__ # => int
print np.zeros(3)[0].__class__.__name__ # => float64
print np.ones(3)[0].__class__.__name__ # => float64
# float16, float32, float64にも対応

# 等差数列
print np.arange(1,11,2) # => [1 3 5 7 9] (要素はint64)

# 分割
print np.linspace(1,11,5) # => [ 1.    3.5   6.    8.5  11. ] (要素はfloat64)
