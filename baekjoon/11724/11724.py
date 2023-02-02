'''
연결 요소의 개수 python 풀이
https://doctcoder.tistory.com/entry/%EC%97%B0%EA%B2%B0-%EC%9A%94%EC%86%8C%EC%9D%98-%EA%B0%9C%EC%88%98-%ED%92%80%EC%9D%B4
'''
import sys
sys.setrecursionlimit(100000)

def dfs(v):
	visit[v]=True
	for i in mat[v]:
		if not visit[i]:
			visit[i]=True
			dfs(i)

n,m=map(int,input().split())
mat=[[] for i in range(n+1)]
cnt=0
for i in range(m):
	a,b=map(int,sys.stdin.readline().split())
	mat[a].append(b)
	mat[b].append(a)
visit=[False]*(n+1)
for i in range(1,n+1):
	if not visit[i]:
		dfs(i)
		cnt+=1
print(cnt)
