'''
소인수분해 python 풀이
https://doctcoder.tistory.com/entry/%EC%86%8C%EC%9D%B8%EC%88%98%EB%B6%84%ED%95%B4-%ED%92%80%EC%9D%B4
'''
n=int(input())
div=2
while 1:
	while n%div==0:
		print(div)
		n/=div
	div+=1
	if n==1: break
