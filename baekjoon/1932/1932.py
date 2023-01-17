'''
정수 삼각형 python 풀이
https://doctcoder.tistory.com/entry/%EC%A0%95%EC%88%98-%EC%82%BC%EA%B0%81%ED%98%95-%ED%92%80%EC%9D%B4
'''
n=int(input())
arr=[]
for i in range(n):
	arr.append(list(map(int,input().split())))
for i in range(1,n):
	for j in range(i+1):
		if j==0: arr[i][j]=arr[i][j]+arr[i-1][j]
		elif j==i: arr[i][j]=arr[i][j]+arr[i-1][j-1]
		else: arr[i][j]=max(arr[i-1][j-1],arr[i-1][j])+arr[i][j]
print(max(arr[n-1]))
