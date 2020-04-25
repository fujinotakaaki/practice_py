# coding:utf-8
import math
from sympy import *

print "\n極限値の計算"
x = symbols('x')
f = ((3+x)**2-3**2)/x
print limit(f, x, 0) # => 6

g = (1/x)**x
print limit(g, x, 0) # => 1

h = (1+1/x)**x
# o(オー)2個で無限の代わり
print limit(h, x, oo) # => E

print limit(log(1+x)/x, x, 0) # => 1
print limit(sin(x)/x, x, 0) # => 1


print "\n微分"
print diff( 1/x, x ) # => -1/x**2
print diff( x, x ) # => 1
print diff( 100, x ) # => 0
print diff( log(x), x ) # =>1/x
print diff( E**x, x, 1)


print "\n積分"
print integrate(2*x, x) # x**2
print integrate(E, x) # E*x
print integrate(log(x), x) # x*log(x) - x
print integrate(sin(x), x) # -cos(x)
print integrate(sin(x**2), x) # 3*sqrt(2)*sqrt(pi)*fresnels(sqrt(2)*x/sqrt(pi))*gamma(3/4)/(8*gamma(7/4))


print "\n定積分"
f1 = E**(-x**2)
print integrate(f1, (x, -oo, oo)) # => sqrt(pi)
f2 = sin(x)/x
print integrate(f2, (x, -oo, oo)) # => pi




