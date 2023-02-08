'''
숨바꼭질 python 풀이
https://doctcoder.tistory.com/entry/%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%88-%ED%92%80%EC%9D%B4
'''
from collections import deque

def bfs(a):
	q=deque([a])
	while q:
		b=q.popleft()
		if b==k: 
			return visited[b]
		for i in (b-1,b+1,2*b):
			if 0<=i<=100000 and not visited[i]:
				visited[i]=visited[b]+1
				q.append(i)

n,k=map(int,input().split())
visited=[0 for i in range(100001)]
print(bfs(n))
