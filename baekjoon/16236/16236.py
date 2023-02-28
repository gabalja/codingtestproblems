'''
아기 상어 python 풀이
https://doctcoder.tistory.com/entry/%EC%95%84%EA%B8%B0-%EC%83%81%EC%96%B4-%ED%92%80%EC%9D%B4
'''
from collections import deque

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
pos = []
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            pos.append(i)
            pos.append(j)
cnt = 0
def bfs(x, y):
    visited = [[0]*N for _ in range(N)]
    queue = deque([[x,y]])
    cand = []
    visited[x][y] = 1
    while queue:
        i, j = queue.popleft()
        for idx in range(4):
            ii, jj = i + dx[idx] , j + dy[idx]
            if 0 <= ii and ii < N and 0 <= jj and jj < N and visited[ii][jj] == 0:
                if space[x][y] > space[ii][jj] and space[ii][jj] != 0:
                    visited[ii][jj] =  visited[i][j] + 1
                    cand.append((visited[ii][jj] - 1, ii, jj))
                elif space[x][y] == space[ii][jj]:
                    visited[ii][jj] =  visited[i][j] + 1
                    queue.append([ii,jj])
                elif space[ii][jj] == 0:
                    visited[ii][jj] =  visited[i][j] + 1
                    queue.append([ii,jj])
    return sorted(cand, key = lambda x: (x[0], x[1], x[2]))
i, j = pos
size = [2, 0]
while True:
    space[i][j] = size[0]
    cand = deque(bfs(i,j))   
    if not cand:
        break        
    step, xx, yy = cand.popleft()
    cnt += step
    size[1] += 1
    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0
    space[i][j] = 0
    i, j = xx, yy       
print(cnt)
