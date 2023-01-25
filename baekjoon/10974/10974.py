'''
모든 순열 python 풀이
https://doctcoder.tistory.com/entry/%EB%AA%A8%EB%93%A0-%EC%88%9C%EC%97%B4-%ED%92%80%EC%9D%B4
'''
from itertools import permutations

n=int(input())
arr=[i+1 for i in range(n)]
res=permutations(arr)
for i in res:
	print(*i)
