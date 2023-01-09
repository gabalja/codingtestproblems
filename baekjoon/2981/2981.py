'''
검문 python 풀이
https://doctcoder.tistory.com/entry/%EA%B2%80%EB%AC%B8-%ED%92%80%EC%9D%B4
'''
import math

n=int(input())
arr=[]
for i in range(n):
	arr.append(int(input()))
arr.sort()
narr=[]
for i in range(1,n):
	narr.append(arr[i]-arr[i-1])
temp=narr[0]
for i in range(1,n-1):
	temp=math.gcd(temp,narr[i])
result=[]
for i in range(2,int(temp**0.5)+1):
	if temp%i==0:
		result.append(i)
		result.append(temp//i)
result.append(temp)
result=list(set(result))
result.sort()
for i in result:
	print(i, end=' ')
