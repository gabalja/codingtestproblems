'''
연구소 python 풀이
https://doctcoder.tistory.com/entry/%EC%97%B0%EA%B5%AC%EC%86%8C-%ED%92%80%EC%9D%B4
'''
import sys; input = sys.stdin.readline
import copy
from itertools import combinations

def solve():
    global answer
    # 새롭게 세울 벽 3개의 모든 조합 얻기
    for wall_combi in combinations(empty, wall_num):
        # 기존 맵 정보 깊은 복사(Deep Copy)
        board_new = copy.deepcopy(board)
        for x_w, y_w in wall_combi:
            board_new[x_w][y_w] = 1
        # 바이러스 위치
        virus = [(n, m) for n in range(N) for m in range(M) if board_new[n][m] == 2]
        # 바이러스마다 전파 끝날 때까지 반복
        while virus:
            x_v, y_v = virus.pop()
            for dx, dy in direction:
                nx = x_v + dx
                ny = y_v + dy
                if 0 <= nx < N and 0 <= ny < M and board_new[nx][ny] == 0:
                    board_new[nx][ny] = 2
                    virus.append((nx, ny)) # 바이러스 전파
        # 안전지대 개수 카운팅
        safezone_cnt = 0
        for row in board_new:
            safezone_cnt += row.count(0)
        answer = max(answer, safezone_cnt)

if __name__ == "__main__":
    N, M = map(int, input().split())
    wall_num = 3
    board = [list(map(int, input().split())) for _ in range(N)]
    # 벽을 세울 수 있는 빈 공간 정보를 리스트에 저장
    empty = [(n, m) for n in range(N) for m in range(M) if board[n][m] == 0]
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    answer = 0
    solve()
    print(answer)
