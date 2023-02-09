'''
트리 순회 python 풀이
https://doctcoder.tistory.com/entry/%ED%8A%B8%EB%A6%AC-%EC%88%9C%ED%9A%8C-%ED%92%80%EC%9D%B4
'''
def pre(t):
	if t != '.':
		print(t, end='')
		pre(tree[t][0])
		pre(tree[t][1])

def ino(t):
	if t != '.':
		ino(tree[t][0])
		print(t, end='')
		ino(tree[t][1])

def pos(t):
	if t != '.':
		pos(tree[t][0])
		pos(tree[t][1])
		print(t, end='')

n = int(input())
tree = {}
for i in range(n):
	rt, l, r = input().split()
	tree[rt] = [l, r]
pre('A')
print()
ino('A')
print()
pos('A')
