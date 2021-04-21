# 리스트 자료형
# 여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형
#   - 배열이나 테이블이라 부르기도 한다.

# 리스트 컴프리헨션 (리스트 초기화)
array = [i for i in range(10)]
print(array)
# 조건문 포함도 가능
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 이차원 리스트 초기화
n = 3
m = 3
array = [[0]*m for _ in range(n)]
array[0][1] = 1
print(array)
array = [[0 for _ in range(3)] for i in range(3)]
array[0][2] = 1
print(array)

# 리스트에 특정 값을 가지는 원소를 모두 제거하기
a = [1,2,3,4,5,5,5]
remove_set = {3,5} # 3과 5를 모두 지우겠땅
result = [i for i in a if i not in remove_set] # a에 있는 원소들을 저장할껀데, remove_set에 들어있다면 포함하지 않겠다.
print(result)