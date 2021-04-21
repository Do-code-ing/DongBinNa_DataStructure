# 집합 자료형

# 중복을 허용하지 않는다.
# 순서가 없다.
# 데이터 조회 및 수정은 O(1)인 상수 시간에 처리할 수 있다.

a = (1,2,3,3)
print(type(a))
a = set(a)
print(a)

b = {4,5,6}
b.add(2)
b.update("1")
print(b)

a = "s1"
b = 123
c = (1,2,3)
d = [1,2,3]
e = {1,2,3}
d.remove(2)
print(d)