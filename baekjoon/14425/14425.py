'''
문자열 집합 python 풀이
https://doctcoder.tistory.com/entry/%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%A7%91%ED%95%A9-%ED%92%80%EC%9D%B4
'''
n,m=map(int,input().split())
sn={input() for i in range(n)}
cnt=0
for i in range(m):
	if input() in sn: cnt+=1
print(cnt)
