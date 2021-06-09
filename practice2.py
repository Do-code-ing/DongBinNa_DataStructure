from collections import deque
import sys
input = sys.stdin.readline

def D(n):
    return (2 * n) % 10000

def S(n):
    if n == 0:
        return 9999
    else:
        return n-1

def L(n):
    return ((n % 1000) * 10) + (n // 1000)

def R(n):
    return (n // 10) + ((n % 10) * 1000)

def solution():
    a, b = map(int, input().split())
    visit = [False] * 10000
    visit[a] = True
    q = deque([(a, "")])
    while q:
        n, dp = q.popleft()
        print(n, dp)
        if n == b:
            print(dp)
            return
        
        x = D(n)
        if not visit[x]:
            visit[x] = True
            q.append((x, dp + "D"))

        x = S(n)
        if not visit[x]:
            visit[x] = True
            q.append((x, dp + "S"))

        x = L(n)
        if not visit[x]:
            visit[x] = True
            q.append((x, dp + "L"))

        x = R(n)
        if not visit[x]:
            visit[x] = True
            q.append((x, dp + "R"))

T = int(input())
for _ in range(T):
    solution()

# D = 2n mod 10000
# S = n-1 if n != 0 else 9999
# L = popleft() and append()
# R = pop() and appendleft()