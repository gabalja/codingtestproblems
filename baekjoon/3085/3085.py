'''
사탕 게임 python 풀이
https://doctcoder.tistory.com/entry/%EC%82%AC%ED%83%95-%EA%B2%8C%EC%9E%84-%ED%92%80%EC%9D%B4
'''
def check(arr):
	n=len(arr)
	ans=1
	for i in range(n):
		cnt=1
		for j in range(1,n):
			if arr[i][j]==arr[i][j-1]: cnt+=1
			else: cnt=1
			if cnt>ans: ans=cnt
		cnt=1
		for j in range(1,n):
			if arr[j][i]==arr[j-1][i]: cnt+=1
			else: cnt=1
			if cnt>ans: ans=cnt
	return ans

n=int(input())
inp=[list(input()) for i in range(n)]
res=0
for i in range(n):
	for j in range(n):
		if j+1<n:
			inp[i][j],inp[i][j+1]=inp[i][j+1],inp[i][j]
			temp=check(inp)
			if temp>res: res=temp
			inp[i][j],inp[i][j+1]=inp[i][j+1],inp[i][j]
		if i+1<n:
			inp[i][j],inp[i+1][j]=inp[i+1][j],inp[i][j]
			temp=check(inp)
			if temp>res: res=temp
			inp[i][j],inp[i+1][j]=inp[i+1][j],inp[i][j]
print(res)
