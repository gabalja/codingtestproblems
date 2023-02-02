'''
이분 그래프 python 풀이
https://doctcoder.tistory.com/entry/%EC%9D%B4%EB%B6%84-%EA%B7%B8%EB%9E%98%ED%94%84-%ED%92%80%EC%9D%B4
'''
import sys
sys.setrecursionlimit(100000)

def dfs(v,a):
	global res
	if res: return
	visit[v]=a
	for i in mat[v]:
		if not visit[i]:
			dfs(i,-a)
		elif visit[v]==visit[i]:
			res=True
			return

k=int(input())
for _ in range(k):
	v,e=map(int,sys.stdin.readline().split())
	mat=[[] for _ in range(v+1)]
	visit=[False]*(v+1)
	for i in range(e):
		a,b=map(int,sys.stdin.readline().split())
		mat[a].append(b)
		mat[b].append(a)
	res=False
	for i in range(1,v+1):
		if not visit[i]:
			dfs(i,1)
			if res: break
	print('NO' if res else 'YES')
