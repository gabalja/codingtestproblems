'''
카잉 달력 python 풀이
https://doctcoder.tistory.com/entry/%EC%B9%B4%EC%9E%89-%EB%8B%AC%EB%A0%A5-%ED%92%80%EC%9D%B4
'''
for i in range(int(input())):
	m,n,x,y=map(int,input().split())
	k=x
	while 1:
		if k>m*n: 
			print(-1)
			break
		if (k-x)%m==0 and (k-y)%n==0:
			print(k)
			break
		k+=m
