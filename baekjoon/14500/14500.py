'''
테트로미노 python 풀이
https://doctcoder.tistory.com/entry/%ED%85%8C%ED%8A%B8%EB%A1%9C%EB%AF%B8%EB%85%B8-%ED%92%80%EC%9D%B4
'''
def dfs(r,c,idx,total):
	global res
	if res>=total+maxs*(3-idx): return
	if idx==3:
		res=max(res,total)
		return
	else:
		for i in range(4):
			nr=r+dr[i]
			nc=c+dc[i]
			if 0<=nr<n and 0<=nc<m and check[nr][nc]==0:
				if idx==1:
					check[nr][nc]=1
					dfs(r,c,idx+1,total+arr[nr][nc])
					check[nr][nc]=0
				check[nr][nc]=1
				dfs(nr,nc,idx+1,total+arr[nr][nc])
				check[nr][nc]=0

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for i in range(n)]
check=[[0]*m for i in range(n)]
dr=[-1,0,1,0]
dc=[0,1,0,-1]
res=0
maxs=max(map(max,arr))
for i in range(n):
	for j in range(m):
		check[i][j]=1
		dfs(i,j,0,arr[i][j])
		check[i][j]=0
print(res)
