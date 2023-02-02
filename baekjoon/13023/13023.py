'''
ABCDE python 풀이
https://doctcoder.tistory.com/entry/ABCDE-%ED%92%80%EC%9D%B4
'''
def dfs(depth,idx):
	global res
	if depth==4:
		res=True
		return
	for i in connect[idx]:
		if not visit[i]:
			visit[i]=True
			dfs(depth+1,i)
			visit[i]=False

n,m=map(int,input().split())
connect=[[] for i in range(n)]
visit=[False]*n
res=False
for i in range(m):
	a,b=map(int,input().split())
	connect[a].append(b)
	connect[b].append(a)
for i in range(n):
	visit[i]=True
	dfs(0,i)
	visit[i]=False
	if res: break
if res: print(1)
else: print(0)
