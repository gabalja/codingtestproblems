'''
A+B - 8 python 풀이
https://doctcoder.tistory.com/entry/AB-8-%ED%92%80%EC%9D%B4
'''
t=int(input())
for i in range(t):
	a,b= map(int,input().split())
	print(f"Case #{i+1}: {a} + {b} = {a+b}")
