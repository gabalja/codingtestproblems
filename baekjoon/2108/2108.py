'''
통계학 python 풀이
https://doctcoder.tistory.com/entry/%ED%86%B5%EA%B3%84%ED%95%99-%ED%92%80%EC%9D%B4
'''
import sys
from collections import Counter

n = int(sys.stdin.readline())
inp = []
for i in range(n):
	inp.append(int(sys.stdin.readline()))
inp.sort()
cnt=Counter(inp).most_common()
ncnt=0
if len(cnt)>1:
	if cnt[0][1]==cnt[1][1]: ncnt=cnt[1][0]
	else: ncnt=cnt[0][0]
else: ncnt=cnt[0][0]
print(round(sum(inp)/n))
print(inp[n//2])
print(ncnt)
print(inp[-1]-inp[0])
