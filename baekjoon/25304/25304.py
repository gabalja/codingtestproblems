'''
영수증 python 풀이
https://doctcoder.tistory.com/entry/%EC%98%81%EC%88%98%EC%A6%9D
'''
x=int(input())
n=int(input())
for i in range(n):
	a,b=map(int,input().split())
	x-=a*b
if(x==0): print("Yes")
else: print("No")
