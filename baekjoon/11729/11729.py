'''
하노이 탑 이동 순서 python 풀이
https://doctcoder.tistory.com/entry/%ED%95%98%EB%85%B8%EC%9D%B4-%ED%83%91-%EC%9D%B4%EB%8F%99-%EC%88%9C%EC%84%9C-%ED%92%80%EC%9D%B4
'''
import math

def hanoi(t,a,b,c):
	if t==1: print(a,b)
	else:
		hanoi(t-1,a,c,b)
		print(a,b)
		hanoi(t-1,c,b,a)

n=int(input())
print(int(math.pow(2,n))-1)
hanoi(n,1,3,2)
