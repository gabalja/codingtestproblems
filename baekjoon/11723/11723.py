'''
집합 python 풀이
https://doctcoder.tistory.com/entry/%EC%A7%91%ED%95%A9-%ED%92%80%EC%9D%B4
'''
import sys 

m=int(sys.stdin.readline())
s=set()
for _ in range(m):
	inp=list(sys.stdin.readline().split())
	if len(inp)!=2:
		if inp[0]=="all":
			s=set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
		else: s=set()
	else:
		ord,num=inp[0],int(inp[1])
		if ord=="add": s.add(num)
		elif ord=="remove": 
			if num in s: s.remove(num)
		elif ord=="check": print(1 if num in s else 0)
		else: 
			if num in s: s.remove(num)
			else: s.add(num)
