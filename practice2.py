import sys
input = sys.stdin.readline

def find_tree(i_start, i_end, p_start, p_end):
    if i_start > i_end or p_start > p_end:
        return
    
    # print(postorder[p_end], end=" ")
    mid = inorder.index(postorder[p_end])
    print(p_end)
    find_tree(i_start, mid-1, p_start, mid)
    find_tree(mid+1, i_end, mid, p_end-1)

if __name__ == "__main__":
    n = int(input())
    inorder = list(map(int, input().split()))
    postorder = list(map(int, input().split()))

    find_tree(0, n-1, 0, n-1)