'''
벽 부수고 이동하기 4 python 풀이
https://doctcoder.tistory.com/entry/%EB%B2%BD-%EB%B6%80%EC%88%98%EA%B3%A0-%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0-4-%ED%92%80%EC%9D%B4
'''
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    cnt = 1
    while q:
        i, j = q.popleft()
        zeros[i][j] = group
        for idx in range(4):
            ni, nj = i + dy[idx], j + dx[idx]
            if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj] or graph[ni][nj] == 1:
                continue
            visited[ni][nj] = True
            q.append((ni, nj))
            cnt += 1
    return cnt

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
zeros = [[0] * m for _ in range(n)]
group = 1
info = {}
info[0] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            w = bfs((i, j))
            info[group] = w
            group += 1

for i in range(n):
    for j in range(m):
        addList = set()
        if graph[i][j]:
            for idx in range(4):
                ni, nj = i + dy[idx], j + dx[idx]
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue
                addList.add(zeros[ni][nj])
            for add in addList:
                graph[i][j] += info[add]
                graph[i][j] %= 10

for g in graph:
    print("".join(map(str, g)))
