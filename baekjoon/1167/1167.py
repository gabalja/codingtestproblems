'''
트리의 지름 python 풀이
https://doctcoder.tistory.com/entry/1167%EB%B2%88-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%A7%80%EB%A6%84-%ED%92%80%EC%9D%B4
'''
from collections import deque

def bfs(st):
	visit=[-1]*(v+1)
	q=deque()
	q.append(st)
	visit[st]=0
	maxs=[0,0]
	while q:
		b=q.popleft()
		for n,m in tree[b]:
			if visit[n]==-1:
				visit[n]=visit[b]+m
				q.append(n)
				if maxs[0]<visit[n]:
					maxs=visit[n],n
	return maxs

v=int(input())
tree=[[] for i in range(v+1)]
for i in range(v):
	a=list(map(int,input().split()))
	for j in range(1,len(a)-2,2):
		tree[a[0]].append((a[j],a[j+1]))
rad,k=bfs(1)
rad,k=bfs(k)
print(rad)
