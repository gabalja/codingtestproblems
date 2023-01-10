'''
괄호 python 풀이
https://doctcoder.tistory.com/entry/%EA%B4%84%ED%98%B8-%ED%92%80%EC%9D%B4
'''
import sys

n=int(input())
for i in range(n):
	stack=[]
	inp=sys.stdin.readline().strip()
	for j in inp:
		if j=='(': stack.append(j)
		elif j==')':
			if stack: stack.pop()
			else:
				print("NO")
				break
	else:
		if stack: print("NO")
		else: print("YES")
