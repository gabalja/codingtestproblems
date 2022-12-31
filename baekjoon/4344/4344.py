'''
평균은 넘겠지 python 풀이
https://doctcoder.tistory.com/entry/%ED%8F%89%EA%B7%A0%EC%9D%80-%EB%84%98%EA%B2%A0%EC%A7%80-%ED%92%80%EC%9D%B4
'''
c=int(input())
for i in range(c):
	sre=list(map(int,input().split()))
	mean=0
	n=sre[0]
	del sre[0]
	for j in range(n):
		mean+=sre[j]
	mean/=n
	per=0
	for j in range(n):
		if(sre[j]>mean): per+=1
	per=per/n*100
	print(f'{round(per,3):.3f}%')
