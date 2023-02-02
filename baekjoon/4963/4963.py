'''
섬의 개수 python 풀이
https://doctcoder.tistory.com/entry/%EC%84%AC%EC%9D%98-%EA%B0%9C%EC%88%98-%ED%92%80%EC%9D%B4
'''
import sys
sys.setrecursionlimit(100000)

def dfs(a,b,c,d):
	inp[a][b]=2
	for i in range(8):
		na,nb=a+dx[i],b+dy[i]
		if 0<=na<h and 0<=nb<w:
			if inp[na][nb]==1:
				dfs(na,nb,c,d)
	return 1

dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]
while 1:
	w,h=map(int,input().split())
	if w==0 and h==0: break
	inp=[list(map(int,input().split())) for i in range(h)]
	cnt=0
	for i in range(h):
		for j in range(w):
			if inp[i][j]==1:
				cnt+=dfs(i,j,w,h)
	print(cnt)
