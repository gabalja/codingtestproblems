'''
링크와 스타트 python 풀이
https://doctcoder.tistory.com/entry/%EB%A7%81%ED%81%AC%EC%99%80-%EC%8A%A4%ED%83%80%ED%8A%B8-%ED%92%80%EC%9D%B4
'''
from itertools import combinations

def diffs(st,li):
	ss,sl=0,0
	for i,j in combinations(st,2):
		ss+=arr[i][j]+arr[j][i]
	for i,j in combinations(li,2):
		sl+=arr[i][j]+arr[j][i]
	return abs(ss-sl)

n=int(input())
arr=[list(map(int,input().split())) for i in range(n)]
visit=list(range(n))
cnt=10000000
for i in range(1,n//2+1):
	st=list(combinations(visit,i))
	li=list(combinations(visit,n-i))
	leng=len(st)
	for j in range(leng):
		diff=diffs(st[j],li[leng-j-1])
		cnt=min(cnt,diff)
print(cnt)
