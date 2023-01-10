'''
에디터 python 풀이
https://doctcoder.tistory.com/entry/%EC%97%90%EB%94%94%ED%84%B0-%ED%92%80%EC%9D%B4
'''
import sys

lstack=list(input())
rstack=[]
	
n=int(input())
for i in range(n):
	inp=sys.stdin.readline().split()
	if inp[0]=="L" and lstack:
		rstack.append(lstack.pop())
	elif inp[0]=="D" and rstack:
		lstack.append(rstack.pop())
	elif inp[0]=="B" and lstack:
		lstack.pop()
	elif inp[0]=="P":
		lstack.append(inp[1])
print("".join(lstack+list(reversed(rstack))))
