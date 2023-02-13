'''
트리의 지름 python 풀이
https://doctcoder.tistory.com/entry/1967%EB%B2%88-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%A7%80%EB%A6%84-%ED%92%80%EC%9D%B4
'''
import sys
sys.setrecursionlimit(10**9)

def dfs(st,p):
	for i in tree[st]:
		a,b=i
		if dis[a]==-1:
			dis[a]=p+b
			dfs(a,p+b)

n=int(input())
tree=[[] for i in range(n+1)]
for i in range(n-1):
	a,b,c=map(int,input().split())
	tree[a].append([b,c])
	tree[b].append([a,c])
dis=[-1]*(n+1)
dis[1]=0
dfs(1,0)
ldis=dis.index(max(dis))
dis=[-1]*(n+1)
dis[ldis]=0
dfs(ldis,0)
print(max(dis))
