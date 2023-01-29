'''
스타트와 링크 python 풀이
https://doctcoder.tistory.com/entry/%EC%8A%A4%ED%83%80%ED%8A%B8%EC%99%80-%EB%A7%81%ED%81%AC-%ED%92%80%EC%9D%B4
'''
def dfs(l,idx):
	global cnt
	if l==n//2:
		a=0
		b=0
		for i in range(n):
			for j in range(n):
				if visit[i] and visit[j]:
					a+=arr[i][j]
				elif not visit[i] and not visit[j]:
					b+=arr[i][j]
		cnt=min(cnt,abs(a-b))
		return
	for i in range(idx,n):
		if not visit[i]:
			visit[i]=True
			dfs(l+1,i+1)
			visit[i]=False

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
visit=[False for i in range(n+1)]
cnt=1000000000000
dfs(0,0)
print(cnt)
