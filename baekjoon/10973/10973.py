'''
이전 순열 python 풀이
https://doctcoder.tistory.com/entry/%EC%9D%B4%EC%A0%84-%EC%88%9C%EC%97%B4-%ED%92%80%EC%9D%B4
'''
n=int(input())
inp=list(map(int,input().split()))
for i in range(n-1,0,-1):
	if inp[i-1]>inp[i]:
		for j in range(n-1,0,-1):
			if inp[i-1]>inp[j]:
				inp[i-1],inp[j]=inp[j],inp[i-1]
				inp=inp[:i]+sorted(inp[i:],reverse=True)
				print(*inp)
				exit(0)
print(-1)
