import sys
input = sys.stdin.readline
INF = sys.maxsize

def order(dp, i, j, arr):
    if dp[i][j] == -1:
        return
    
    x = dp[i][j]
    order(dp, i, x, arr)
    arr.append(x)
    order(dp, x, j, arr)
    

def solution():
    n = int(input())
    graph = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        graph[i][i] = 0
    
    m = int(input())
    for _ in range(m):
        a, b, c = map(int, input().split())
        if graph[a][b] > c:
            graph[a][b] = c
    
    dp = [[-1] * (n+1) for _ in range(n+1)]
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                value = graph[i][k] + graph[k][j]
                if graph[i][j] > value:
                    graph[i][j] = value
                    dp[i][j] = k
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(graph[i][j] if graph[i][j] != INF else 0, end=" ")
        print()
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j or graph[i][j] == INF:
                print(0)
            else:
                arr = [i]
                order(dp, i, j, arr)
                arr += [j]
                print(len(arr), " ".join(map(str, arr)))
    
solution()