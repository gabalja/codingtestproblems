'''
오등큰수 python 풀이
https://doctcoder.tistory.com/entry/%EC%98%A4%EB%93%B1%ED%81%B0%EC%88%98-%ED%92%80%EC%9D%B4
'''
from collections import Counter

n=int(input())
inp=list(map(int,input().split()))
stack=[]
res=[-1 for i in range(n)]
cnt=Counter(inp)
for i in range(n):
	while stack and cnt[inp[stack[-1]]]<cnt[inp[i]]:
		res[stack.pop()]=inp[i]
	stack.append(i)
print(*res)
