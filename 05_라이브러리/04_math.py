# math

# 최대 공약수, 최소 공배수 구해줌

# 최대 공약수
# gcd(integer)

from math import *

a = 21
b = 14
print(gcd(a, b))

# 최소 공배수
# lcm(integer)

print(lcm(a, b))

# 최소 공배수 알고리즘
def lcm2(a, b):
    return a*b // gcd(a,b)