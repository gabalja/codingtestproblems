'''
두 동전 python 풀이
https://doctcoder.tistory.com/entry/%EB%91%90-%EB%8F%99%EC%A0%84-%ED%92%80%EC%9D%B4
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N,M = map(int,input().split())
board = [list(input().rstrip()) for _ in range(N)]
visited = []
coinpos = []

dx = [-1,0,1,0]
dy = [0,-1,0,1]

res = 2147000000

def DFS(coin1, coin2, cnt):
    global res
    x1,y1 = coin1
    x2,y2 = coin2
    if cnt>=res or cnt>10:
        return
    if x1 == x2 and y1 == y2:
        return
    if (0 > x1 or N <= x1 or 0 > y1 or M <= y1) and (0 > x2 or N <= x2 or 0 > y2 or M <= y2):
        return
    if (0 > x1 or N <= x1 or 0 > y1 or M <= y1) or (0 > x2 or N <= x2 or 0 > y2 or M <= y2):
        res = min(res,cnt)
        return
    for i in range(4):
        nx1 = x1 + dx[i]
        ny1 = y1 + dy[i]
        nx2 = x2 + dx[i]
        ny2 = y2 + dy[i]
        if 0<=nx1<N and 0<=ny1<M and 0<=nx2<N and 0<=ny2<M:
            if board[nx1][ny1] != '#' and board[nx2][ny2] != '#' and (nx1,ny1,nx2,ny2) not in visited:
                visited.append((nx1,ny1,nx2,ny2))
                DFS((nx1,ny1),(nx2,ny2), cnt+1)
                visited.pop()
            elif board[nx1][ny1] == '#' and board[nx2][ny2] != '#' and (x1,y1,nx2,ny2) not in visited:
                visited.append((x1,y1,nx2,ny2))
                DFS((x1,y1),(nx2,ny2),cnt+1)
                visited.pop()
            elif board[nx1][ny1] != '#' and board[nx2][ny2] == '#' and (nx1,ny1,x2,y2) not in visited:
                visited.append((nx1,ny1,x2,y2))
                DFS((nx1,ny1),(x2,y2),cnt+1)
                visited.pop()
        else:
            visited.append((nx1,ny1,nx2,ny2))
            DFS((nx1,ny1),(nx2,ny2), cnt+1)
            visited.pop()


for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coinpos.append((i,j))

DFS(coinpos[0],coinpos[1],0)
print(res) if res<=10 else print(-1)
