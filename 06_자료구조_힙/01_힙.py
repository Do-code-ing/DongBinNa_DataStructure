# [힙(Heap)의 특징]

# 힙은 완전 이진 트리 자료구조의 일종입니다.
# 힙에서 항상 루트 노드(root node)를 제거합니다.

# 최소 힙(min heap)
#   - 루트 노드가 가장 작은 값을 가집니다.
#   - 따라서 값이 작은 데이터가 우선적으로 제거됩니다.

# 최대 힙(max heap)
#   - 루트 노드가 가장 큰 값을 가집니다.
#   - 따라서 값이 큰 데이터가 우선적으로 제거됩니다.


# [완전 이진 트리(Complete Binary Tree)]

# 완전 이진 트리란 루트(root) 노드부터 시작하여
# 왼쪽 자식 노드, 오른쪽 자식 노드 순서대로 데이터가 차례대로 삽입되는 트리(tree)를 의미합니다.


# [최소 힙 구성 함수: Min-Heapify()]

# (상향식) 부모 노드로 거슬러 올라가며, 부모보다 자신의 값이 더 작은 경우에 위치를 교체합니다.

# 1. 힙에 새로운 원소가 삽입될 때
# 새로운 원소가 삽입되었을 때 O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있습니다.

# 2. 힙에서 원소가 제거될 때
# 원소가 제거되었을 때 O(logN)의 시간 복잡도로 힙 성질을 유지하도록 할 수 있습니다.
#   - 원소를 제거할 때는 가장 마지막 노드가 루트 노드의 위치에 오도록 합니다.
#   - 이후에 루트 노드에서부터 하향식으로(더 작은 자식 노드로) Heapify()를 진행합니다.


# [우선순위 큐 라이브러리를 활용한 힙 정렬 구현 예제]

import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    
    return result

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
    print(res[i])