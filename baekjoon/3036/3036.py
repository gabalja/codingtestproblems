'''
링 python 풀이
https://doctcoder.tistory.com/entry/%EB%A7%81-%ED%92%80%EC%9D%B4
'''
import math

n=int(input())
arr=list(map(int,input().split()))
for i in range(1,n):
	gcds=math.gcd(arr[0],arr[i])
	print(f'{arr[0]//gcds}/{arr[i]//gcds}')
