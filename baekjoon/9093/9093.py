'''
단어 뒤집기 python 풀이
https://doctcoder.tistory.com/entry/%EB%8B%A8%EC%96%B4-%EB%92%A4%EC%A7%91%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
import sys

n=int(input())
for i in range(n):
	inp=list(sys.stdin.readline().split())
	for j in inp:
		print(j[::-1],end=' ')
