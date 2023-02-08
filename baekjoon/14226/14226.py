'''
이모티콘 python 풀이
https://doctcoder.tistory.com/entry/%EC%9D%B4%EB%AA%A8%ED%8B%B0%EC%BD%98-%ED%92%80%EC%9D%B4
'''
from collections import deque

def bfs(a):
	q=deque()
	q.append((1,0))
	visited[1][0]=0
	while q:
		a,b=q.popleft()
		if visited[a][a]==-1: 
			visited[a][a]=visited[a][b]+1
			q.append((a,a))
		if a+b<=s and visited[a+b][b]==-1:
			q.append((a+b,b))
			visited[a+b][b]=visited[a][b]+1
		if a>=1 and visited[a-1][b]==-1:
			q.append((a-1,b))
			visited[a-1][b]=visited[a][b]+1

s=int(input())
visited=[[-1]*1001 for i in range(1001)]
bfs(s)
res=-1
for i in range(s+1):
	if visited[s][i]!=-1:
		if res==-1 or res>visited[s][i]:
			res=visited[s][i]
print(res)
