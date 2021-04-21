# colletions

# 원소가 몇 번씩 등장했는지 알려준다.
# Counter(iterable)
# iterable의 엘리먼트를 key로, 등장횟수를 value하는 사전을 반환한다?

from collections import *
a = Counter([1,1,2,3,4,4,5,5,5])
print(a[1])
# 2
print(a[2])
# 1
print(a[3])
# 1
print(a[4])
# 2
print(a[5])
# 3
print(type(a))
print(dict(a))
# <class 'collections.Counter'>
# {1: 2, 2: 1, 3: 1, 4: 2, 5: 3}