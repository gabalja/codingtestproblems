'''
알파벳 개수 python 풀이
https://doctcoder.tistory.com/entry/%EC%95%8C%ED%8C%8C%EB%B2%B3-%EA%B0%9C%EC%88%98-%ED%92%80%EC%9D%B4
'''
from collections import Counter

inp=input()
alpha="abcdefghijklmnopqrstuvwxyz"
cnt=Counter(inp)
for i in alpha:
	print(cnt[i],end=' ')
