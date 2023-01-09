'''
직각삼각형 python 풀이
https://doctcoder.tistory.com/entry/%EC%A7%81%EA%B0%81%EC%82%BC%EA%B0%81%ED%98%95-%ED%92%80%EC%9D%B4
'''
while 1:
	a,b,c=map(int,input().split())
	if a==0 and b==0 and c==0: break
	if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b: print("right")
	else: print("wrong")
