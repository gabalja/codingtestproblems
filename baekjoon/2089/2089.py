'''
-2진수 python 풀이
https://doctcoder.tistory.com/entry/2%EC%A7%84%EC%88%98-%ED%92%80%EC%9D%B4
'''
n=int(input())
res=""
if n==0: print(0)
else:
	while n:
		if n%-2==0:
			res+='0'
			n//=-2
		else:
			res+='1'
			n=n//-2+1
print(res[::-1])
