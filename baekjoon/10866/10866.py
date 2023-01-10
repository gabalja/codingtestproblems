'''
덱 python 풀이
https://doctcoder.tistory.com/entry/%EB%8D%B1-%ED%92%80%EC%9D%B4
'''
import sys

stacks=[]

def push_back(a):
	stacks.append(a)

def push_front(a):
	stacks.insert(0,a)

def pop_front():
	if len(stacks)==0: print(-1)
	else:
		print(stacks[0])
		del stacks[0]

def pop_back():
	if len(stacks)==0: print(-1)
	else:
		print(stacks[-1])
		del stacks[-1]

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
	if inp=="pop_front": pop_front()
	elif inp=="pop_back": pop_back()
	elif inp=="size": size()
	elif inp=="empty": empty()
	elif inp=="back": back()
	elif inp=="front": front()
	else: 	
		p,q=inp.split()
		if p=="push_back": push_back(q)
		elif p=="push_front": push_front(q)
