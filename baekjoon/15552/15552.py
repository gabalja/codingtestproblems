'''
빠른 A+B python 풀이
https://doctcoder.tistory.com/entry/%EB%B9%A0%EB%A5%B8-AB-%ED%92%80%EC%9D%B4
'''
import sys
t=int(input())
for i in range(t):
	a,b= map(int,sys.stdin.readline().split())
	print(a+b)
