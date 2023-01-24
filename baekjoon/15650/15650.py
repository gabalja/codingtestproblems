'''
N과 M (2) python 풀이
https://doctcoder.tistory.com/entry/N%EA%B3%BC-M-2-%ED%92%80%EC%9D%B4
'''
from itertools import combinations

n,m=map(int,input().split())
arr=[i+1 for i in range(n)]
res=combinations(arr,m)
for i in res:
	for j in i:
		print(j,end=' ')
	print()
