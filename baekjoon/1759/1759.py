'''
암호 만들기 python 풀이
https://doctcoder.tistory.com/entry/%EC%95%94%ED%98%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
from itertools import combinations

l,c=map(int,input().split())
strs=list(input().split())
strs.sort()
vowel=set('aeiou')
res=list(combinations(strs,l))
for i in res:
	check=set(i)-vowel
	c=len(check)
	if c>=2 and l-c>=1:
		print("".join(i))
