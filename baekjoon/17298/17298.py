'''
오큰수 python 풀이
https://doctcoder.tistory.com/entry/%EC%98%A4%ED%81%B0%EC%88%98-%ED%92%80%EC%9D%B4
'''
n=int(input())
inp=list(map(int,input().split()))
stack=[]
res=[-1 for i in range(n)]
for i in range(n):
	while stack and inp[stack[-1]]<inp[i]:
		res[stack.pop()]=inp[i]
	stack.append(i)
print(*res)
