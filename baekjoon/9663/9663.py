'''
N-Queen python 풀이
https://doctcoder.tistory.com/entry/N-Queen-%ED%92%80%EC%9D%B4
'''
def bt(x):
    global cnt
    if x == n:
        cnt += 1

    for i in range(n):
        if visited_1[i] or visited_2[i-x] or visited_3[i+x]:
            continue
        visited_1[i] = 1
        visited_2[i-x] = 1
        visited_3[i+x] = 1
        bt(x+1)
        visited_1[i] = 0
        visited_2[i-x] = 0
        visited_3[i+x] = 0

n = int(input())
cnt = 0
visited_1 = [0] * n
visited_2 = [0] * (2*n-1)
visited_3 = [0] * (2*n-1)

bt(0)
print(cnt)
