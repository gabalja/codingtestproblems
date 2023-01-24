'''
N과 M (11) python 풀이
https://doctcoder.tistory.com/entry/N%EA%B3%BC-M-11-%ED%92%80%EC%9D%B4
'''
from itertools import product

n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
res=list(set(product(arr,repeat=m)))
res.sort()
for i in res:
	for j in i:
		print(j,end=' ')
	print()
