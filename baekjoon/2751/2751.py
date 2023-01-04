'''
수 정렬하기 2 python 풀이
https://doctcoder.tistory.com/entry/%EC%88%98-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-2-%ED%92%80%EC%9D%B4
'''
import sys

n=int(input())
arr=[]
for i in range(n):
	arr.append(int(sys.stdin.readline()))
arr.sort()
for i in range(n):
	print(arr[i])
