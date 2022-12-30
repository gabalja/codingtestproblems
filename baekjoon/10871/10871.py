'''
X보다 작은 수 python 풀이
https://doctcoder.tistory.com/entry/X%EB%B3%B4%EB%8B%A4-%EC%9E%91%EC%9D%80-%EC%88%98-%ED%92%80%EC%9D%B4
'''
n,x=map(int,input().split())
arr=list(map(int,input().split()))
for i in arr:
	if i<x: print(i, end=' ')
