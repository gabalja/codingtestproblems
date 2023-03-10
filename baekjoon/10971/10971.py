'''
외판원 순회 2 python 풀이
https://doctcoder.tistory.com/entry/%EC%99%B8%ED%8C%90%EC%9B%90-%EC%88%9C%ED%9A%8C-2-%ED%92%80%EC%9D%B4
'''
def dfs(st,cur,weight,cnt):
	global res
	if cnt==n:
		if inp[cur][st]:
			weight+=inp[cur][st]
			if res>weight: res=weight
			return
	if weight>res:
		return
	for i in range(n):
		if not visit[i] and inp[cur][i]:
			visit[i]=1
			dfs(st,i,weight+inp[cur][i],cnt+1)
			visit[i]=0
	
n=int(input())
inp=[list(map(int,input().split())) for i in range(n)]
res=100000000
visit=[0]*n
for i in range(n):
	visit[i]=1
	dfs(i,i,0,1)
	visit[i]=0
print(res)
