'''
분해합 python 풀이
https://doctcoder.tistory.com/entry/%EB%B6%84%ED%95%B4%ED%95%A9-%ED%92%80%EC%9D%B4
'''
n=int(input())
for i in range(1,n+1):
	num=sum(map(int,str(i)))+i
	if num==n:
		print(i)
		break
	if i==n:
		print(0)
