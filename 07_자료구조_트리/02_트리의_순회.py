# 트리의 순회 (Tree Traversal)

# 트리 자료구조에 포함된 노드를 특정한 방법으로 한 번씩 방문하는 방법을 의미합니다.
#   - 트리의 정보를 시각적으로 확인할 수 있습니다.
# 대표적인 트리 순회 방법은 다음과 같습니다.
#   - 전위 순회(pre-order traverse): 루트 -> 왼쪽 -> 오른쪽
#   - 중위 순회(in-order traverse): 왼쪽 -> 루트 -> 오른쪽
#   - 후위 순회(post-order traverse): 왼쪽 -> 오른쪽 -> 루트

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회(Preorder Traversal)
def pre_order(node):
    print(node.data, end=" ")
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

# 중위 순회(Inorder Traversal)
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end=" ")
    if node.right_node != None:
        in_order(tree[node.right_node])

# 후위 순회(Postorder Traversal)
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end=" ")

n = int(input())
tree = {}

for _ in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    tree[data] = Node(data, left_node, right_node)

print(tree)

pre_order(tree["A"])
print()
in_order(tree["A"])
print()
post_order(tree["A"])

"""
입력 예시
7
A B C
B D E
C F G
D None None
E None None
F None None
G None None

출력 결과
A B D E C F G
D B E A F C G
D E B F G C A
"""