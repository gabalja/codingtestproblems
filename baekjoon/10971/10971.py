'''
차이를 최대로 python 풀이
https://doctcoder.tistory.com/entry/%EC%B0%A8%EC%9D%B4%EB%A5%BC-%EC%B5%9C%EB%8C%80%EB%A1%9C-%ED%92%80%EC%9D%B4
'''
from itertools import permutations

n=int(input())
inp=list(map(int,input().split()))
per=list(permutations(inp,n))
res=-10000000
for i in per:
	temp=0
	for j in range(n-1):
		temp+=abs(i[j]-i[j+1])
	if temp>res: res=temp
print(res)
