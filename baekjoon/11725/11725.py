'''
트리의 부모 찾기 python 풀이
https://doctcoder.tistory.com/entry/%ED%8A%B8%EB%A6%AC%EC%9D%98-%EB%B6%80%EB%AA%A8-%EC%B0%BE%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
import sys
sys.setrecursionlimit(1000000)

def dfs(st,p):
	for i in tree[st]:
		if p[i]==0:
			p[i]=st
			dfs(i,p)

n=int(input())
tree=[[] for i in range(n+1)]
par=[0 for i in range(n+1)]
for i in range(n-1):
	a,b=map(int,input().split())
	tree[a].append(b)
	tree[b].append(a)
dfs(1,par)
for i in range(2,n+1):
	print(par[i])
