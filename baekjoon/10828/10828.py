'''
스택 python 풀이
https://doctcoder.tistory.com/entry/%EC%8A%A4%ED%83%9D-%ED%92%80%EC%9D%B4
'''
import sys

stacks=[]

def pop():
	if len(stacks)==0: print(-1)
	else:
		print(stacks[-1])
		del stacks[-1]

def size():
	print(len(stacks))

def empty():
	if len(stacks)==0: print(1)
	else: print(0)

def top():
	if len(stacks)==0: print(-1)
	else: print(stacks[-1])

def push(a):
	stacks.append(a)

n=int(input())
for i in range(n):
	inp=sys.stdin.readline().strip()
	if inp=="pop": pop()
	elif inp=="size": size()
	elif inp=="empty": empty()
	elif inp=="top": top()
	else:
		p,q=inp.split()
		push(int(q))
