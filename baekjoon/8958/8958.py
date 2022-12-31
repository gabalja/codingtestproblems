'''
OX퀴즈 python 풀이
https://doctcoder.tistory.com/entry/OX%ED%80%B4%EC%A6%88-%ED%92%80%EC%9D%B4
'''
t=int(input())
for i in range(t):
	res=cul=0
	ox=input()
	for j in ox:
		if(j=='O'):
			cul+=1
			res+=cul
		else: cul=0
	print(res)
