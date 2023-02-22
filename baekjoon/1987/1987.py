'''
알파벳 python 풀이
https://doctcoder.tistory.com/entry/%EC%95%8C%ED%8C%8C%EB%B2%B3-%ED%92%80%EC%9D%B4
'''
import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
answer = 1
def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])])
    while q:
        x, y, ans = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)

BFS(0, 0)
print(answer)
