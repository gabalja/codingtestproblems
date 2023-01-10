'''
요세푸스 문제 python 풀이
https://doctcoder.tistory.com/entry/%EC%9A%94%EC%84%B8%ED%91%B8%EC%8A%A4-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4
'''
n,k=map(int,input().split())
yose=[i+1 for i in range(n)]
res=[]
idx=0
for i in range(n):
	idx+=k-1
	if idx>=len(yose):
		idx%=len(yose)
	res.append(str(yose.pop(idx)))
print('<',', '.join(res),'>',sep='')
