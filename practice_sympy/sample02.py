# coding:utf-8
import math
from sympy import *

# 2元2次方程式の扱い
[x,y] = symbols('x y')
f = (y-2)**2 + (x-2)**2 - 1

# 各変数について解く
x1 = solve(f, x)
y1 = solve(f, y)

print 'x = %s' % x1
# x = [-sqrt(-(y - 3)*(y - 1)) + 2, sqrt(-(y - 3)*(y - 1)) + 2]
print 'y = %s' % y1
# y = [-sqrt(-(x - 3)*(x - 1)) + 2, sqrt(-(x - 3)*(x - 1)) + 2]

# 変数指定なしでも動く(変数名順ですかね？)
print solve(f)
# [{x: -sqrt(-(y - 3)*(y - 1)) + 2}, {x: sqrt(-(y - 3)*(y - 1)) + 2}]

# 2元連立方程式を解く(至言)
g = y - x
print solve([f, g])
# [{x: -sqrt(2)/2 + 2, y: -sqrt(2)/2 + 2}, {x: sqrt(2)/2 + 2, y: sqrt(2)/2 + 2}]
