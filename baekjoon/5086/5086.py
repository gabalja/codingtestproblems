'''
배수와 약수 python 풀이
https://doctcoder.tistory.com/entry/%EB%B0%B0%EC%88%98%EC%99%80-%EC%95%BD%EC%88%98-%ED%92%80%EC%9D%B4
'''
while 1:
	a,b=map(int,input().split())
	if a==0 and b==0: break
	if b%a==0:
		print("factor")
	elif a%b==0:
		print("multiple")
	else:
		print("neither")
