'''
N과 M (9) python 풀이
https://doctcoder.tistory.com/entry/N%EA%B3%BC-M-9-%ED%92%80%EC%9D%B4
'''
from itertools import permutations

n,m=map(int,input().split())
arr=list(map(int,input().split()))
res=list(set(permutations(arr,m)))
res.sort()
for i in res:
	for j in i:
		print(j,end=' ')
	print()
