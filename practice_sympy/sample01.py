# coding:utf-8
import math
from sympy import *

p = Rational(22,7)
print p # =>22/7
print 22./7 # => 3.14285...

# 有効数字と四捨五入の実行
print N(p, 3) # => 3.14
q = N(math.pi, 3)
print q # => 3.14
print N(1.99999, 3) # => 2.00


# Rationalを使った計算
a = Rational(99,70) # √2
b = Rational(193,71) # e
print a + b
print a * b
print a / b
print a ** 2
print sqrt(300)


# 変数(シンボル)
x = symbols('x')
f = x**2 + 2*x + 1
g = x**2 - 2*x + 1 - 1 + 6*x
print f # => x**2 + 2*x + 1

# 因数分解
print factor(f)

# 式展開
print expand((x-1)**2)

# 式の整理
print g

# 方程式を解く(至言)
print solve(f) # => [-1] classはリスト
print solve(g) # => [-4, 0] classはリスト
