# itertools
# 순열과 조합

from itertools import *

# 순열:
# permutations(data, n)
# data에서 n만큼의 경우의 수로 뽑은 목록

# 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
# nPr : 순열의 수
# {a,b,c} -> 'abc','acb','bac','bca','cab','cba


data = ["A","B","C"]
print(list(permutations(data,3)))
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# 조합:
# combinations(data, n)

# nCr : 조합의 수
# {a,b,c} -> 'ab','ac','bc'

data = ["A","B","C"]
print(list(combinations(data, 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

# 중복 순열:
# product(data, repeat=n)

# n^r : 중복순열의 경우의 수

data = ["A","B","C"]
print(list(product(data, repeat=2)))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# 중복 조합:
# combinations_with_replacement(data, n)

# nHr

data = ["A","B","C"]
print(list(combinations_with_replacement(data, 2)))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]