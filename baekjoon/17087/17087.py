'''
숨바꼭질 6 python 풀이
https://doctcoder.tistory.com/entry/%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%88-6-%ED%92%80%EC%9D%B4
'''
import math

n,m=map(int,input().split())
arr=list(map(int,input().split()))
for i in range(n):
	arr[i]=abs(arr[i]-m)
res=arr[0]
for i in range(1,n):
	res=math.gcd(res,arr[i]) 
print(res)
