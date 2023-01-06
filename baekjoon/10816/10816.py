'''
숫자 카드 2 python 풀이
https://doctcoder.tistory.com/entry/%EC%88%AB%EC%9E%90-%EC%B9%B4%EB%93%9C-2-%ED%92%80%EC%9D%B4
'''
from collections import Counter

n=int(input())
card=list(map(int,input().split()))
m=int(input())
num=list(map(int,input().split()))
cnt=Counter(card)
for i in num:
	if i in cnt: print(cnt[i],end=' ')
	else:print(0,end=' ')
