'''
로또 python 풀이
https://doctcoder.tistory.com/entry/%EB%A1%9C%EB%98%90-%ED%92%80%EC%9D%B4
'''
from itertools import combinations

while 1:
	inp=list(map(int,input().split()))
	n=inp[0]
	num=inp[1:]
	if n==0: break
	for i in combinations(num,6):
		for j in i:
			print(j,end=' ')
		print()
	print()
