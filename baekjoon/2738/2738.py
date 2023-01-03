'''
행렬 덧셈 python 풀이
https://doctcoder.tistory.com/entry/%ED%96%89%EB%A0%AC-%EB%8D%A7%EC%85%88-%ED%92%80%EC%9D%B4
'''
n,m=map(int,input().split())
mat=[[0 for i in range(m)]for j in range(n)]
for k in range(2):
	for i in range(n):
		tem=list(map(int,input().split()))
		for j in range(m):
			mat[i][j]+=tem[j]
for i in range(n):
	for j in range(m):
		print(mat[i][j],end=' ')
	print('')
