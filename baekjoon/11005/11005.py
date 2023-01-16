'''
진법 변환 2 python 풀이
https://doctcoder.tistory.com/entry/%EC%A7%84%EB%B2%95-%EB%B3%80%ED%99%98-2-%ED%92%80%EC%9D%B4
'''
n,b=map(int,input().split())
res=""
if n==0: print(0)
else:
	while n:
		a=n%b
		if a>=10:
			res+=chr(a+55)
		else: res+=str(a)
		n//=b
	print(res[::-1])
