'''
가장 긴 바이토닉 부분 수열 python 풀이
https://doctcoder.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EB%B0%94%EC%9D%B4%ED%86%A0%EB%8B%89-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%92%80%EC%9D%B4
'''
n=int(input())
arr=list(map(int,input().split()))
dp1=[1 for i in range(n)]
dp2=[1 for i in range(n)]
res=[0 for i in range(n)]
for i in range(1,n): # 증가
	for j in range(i):
		if arr[j]<arr[i]: dp1[i]=max(dp1[i],dp1[j]+1)
for i in range(n-1,-1,-1): # 감소
	for j in range(n-1,i,-1):
		if arr[j]<arr[i]: dp2[i]=max(dp2[i],dp2[j]+1)
for i in range(n):
	res[i]=dp1[i]+dp2[i]-1
print(max(res))
