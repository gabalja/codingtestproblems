'''
단어 뒤집기 2 python 풀이
https://doctcoder.tistory.com/entry/%EB%8B%A8%EC%96%B4-%EB%92%A4%EC%A7%91%EA%B8%B0-2-%ED%92%80%EC%9D%B4
'''
import sys

inp=list(sys.stdin.readline().rstrip())
i=0
idx=0
while i<len(inp):
	if inp[i]=='<':
		i+=1
		while inp[i]!='>': i+=1
		i+=1
	elif inp[i].isalnum():
		idx=i
		while i<len(inp) and inp[i].isalnum():
			i+=1
		stack=inp[idx:i]
		stack.reverse()
		inp[idx:i]=stack
	else: i+=1
print("".join(inp))
