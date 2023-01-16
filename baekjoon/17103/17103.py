'''
골드바흐 파티션 python 풀이
https://doctcoder.tistory.com/entry/%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90-%ED%8C%8C%ED%8B%B0%EC%85%98-%ED%92%80%EC%9D%B4
'''
import sys, math

input = sys.stdin.readline

n = 1000000
array = [True for i in range(n + 1)]
prime = []
for i in range(2, n + 1):
    if array[i] == True:
        j = 2
        prime.append(i)
        while i * j <= n:
            array[i * j] = False
            j += 1

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for i in range(n // 2 , 1 , -1):
        if array[i] == True and array[n-i] == True:
            cnt += 1
        else:
            continue
    print(cnt)
