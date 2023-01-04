'''
수 정렬하기 3 python 풀이
https://doctcoder.tistory.com/entry/%EC%88%98-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-3-%ED%92%80%EC%9D%B4
'''
import sys

n = int(sys.stdin.readline())
arr = [0 for i in range(10000)]
for i in range(n):
    arr[int(sys.stdin.readline())-1] += 1
for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)
