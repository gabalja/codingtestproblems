'''
N과 M (7) python 풀이
https://doctcoder.tistory.com/entry/N%EA%B3%BC-M-7-%ED%92%80%EC%9D%B4
'''
from itertools import product

n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
res=product(arr,repeat=m)
for i in res:
	for j in i:
		print(j,end=' ')
	print()
