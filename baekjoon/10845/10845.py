'''
큐 python 풀이
https://doctcoder.tistory.com/entry/%ED%81%90-%ED%92%80%EC%9D%B4
'''
import sys

stacks=[]

def push(a):
	stacks.append(a)

def pop():
	if len(stacks)==0: print(-1)
	else:
		print(stacks[0])
		del stacks[0]

def size():
	print(len(stacks))

def empty():
	if len(stacks)==0: print(1)
	else: print(0)

def back():
	if len(stacks)==0: print(-1)
	else: print(stacks[-1])

def front():
	if len(stacks)==0: print(-1)
	else: print(stacks[0])


n=int(input())
for i in range(n):
	inp=sys.stdin.readline().strip()
	if inp=="pop": pop()
	elif inp=="size": size()
	elif inp=="empty": empty()
	elif inp=="back": back()
	elif inp=="front": front()
	else: # push
		p,q=inp.split()
		push(int(q))
