# coding:utf-8
import sys # sys.stdout.write('Hello') で改行なしでHelloが出力可
import math
import numpy as np

# 3x3の正方行列作成
mtx = np.matrix([
list(range(1,4)),
list(range(4,7)),
list(range(7,10))
])
# printの改行を回避するための方法
print "mtx ="
print mtx
# mtx.__class__ = <class 'numpy.matrixlib.defmatrix.matrix'>


# 3x3の単位行列
I3 = np.identity(3)
print "\nI3 = "
print I3
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
# 要素のクラスは<type 'numpy.float64'>

# 対角行列
print '\nnp.diag([8,9,3,1]) = '
print np.diag([8,9,3,1]) # => 4x4の対角行列
# [[8 0 0 0]
#  [0 9 0 0]
#  [0 0 3 0]
#  [0 0 0 1]]

# 四則演算
print '\n和 => '
print mtx + mtx
# [[ 2  4  6]
#  [ 8 10 12]
#  [14 16 18]]

print "\n差 =>"
print mtx - mtx
# [[0 0 0]
#  [0 0 0]
#  [0 0 0]]

print "\n積 => "
print mtx * mtx
# [[ 30  36  42]
#  [ 66  81  96]
#  [102 126 150]]

print "\n商 => "
print mtx / mtx
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]]


# ランダムな行列の作成
vtr = np.random.randint(0,10,5)
print "\nnp.random.randint(0,10,5) = # 0~9の整数の組み合わせで1x5のndarrayを作成"
print vtr

rmtx = np.random.randint(0,10,(3,3))
print "\nnp.random.randint(0,10,(row,column)) = # 0~9の整数の組み合わせで3x3の正方行列を作成"
print rmtx


# 行ごとまたは列ごとの合計値の計算（用途不明）
# np.sum(<matrix>, axis)も可能
mtx_sum_row = mtx.sum(axis = 1)  # 行
print "\n各行の和(mtx):"
print mtx_sum_row

mtx_sum_column = mtx.sum(axis = 0) # 列
print "\n各列の和(mtx):"
print mtx_sum_column

# 行ごとまたは列ごとの平均値
# 平均値： np.mean(<matrix>, axis)も可能
mtx_mean_row = mtx.mean(axis = 1)  # 行
print "\n各行の平均値(mtx):"
print mtx_mean_row

# 中央値探索(ndarray)
ndarray1 = np.array([1,2,4,8,9])
# ndarray1.median()はエラーになる（なんでだ）
print "\nndarrayの中央値:"
print "np.median(np.array([1,2,4,8,9]))= "
print np.median(ndarray1)
# ndarray1は行列でもいける
# axisも指定可能だ


# 行列 => 配列(ndarrayへ, flattenみたいなもの？)
mtx_ravel = mtx.ravel() # => <class 'numpy.matrixlib.defmatrix.matrix'>
print mtx_ravel
print np.median(mtx_ravel)


# 配列 => 行列(matrixへ)
# np.reshape(<ndarray>, (row, column))も可能
print mtx_ravel.reshape((3,3))
