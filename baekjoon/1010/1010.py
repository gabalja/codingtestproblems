'''
다리 놓기 python 풀이
https://doctcoder.tistory.com/entry/%EB%8B%A4%EB%A6%AC-%EB%86%93%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
t=int(input())
for i in range(t):
	n,m=map(int,input().split())
	if n>=m-n: nn=n
	else: nn=m-n
	res=1
	for j in range(1,m-nn+1):
		res=int(res*(m+1-j)/j)
	print(res)
