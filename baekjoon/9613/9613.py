'''
GCD 합 python 풀이
https://doctcoder.tistory.com/entry/GCD-%ED%95%A9-%ED%92%80%EC%9D%B4
'''
import math

n=int(input())
for i in range(n):
	ts=list(map(int,input().split()))
	sum=0
	for j in range(1,ts[0]+1):
		for k in range(j+1,ts[0]+1):
			sum+=math.gcd(ts[j],ts[k])
	print(sum)
