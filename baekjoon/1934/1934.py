'''
최소공배수 python 풀이
https://doctcoder.tistory.com/entry/%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98-%ED%92%80%EC%9D%B4
'''
import math

n=int(input())
for i in range(n):
	a,b=map(int,input().split())
	gcds=math.gcd(a,b)
	print(int(a*b/gcds))
