'''
나는야 포켓몬 마스터 이다솜 python 풀이
https://doctcoder.tistory.com/entry/%EB%82%98%EB%8A%94%EC%95%BC-%ED%8F%AC%EC%BC%93%EB%AA%AC-%EB%A7%88%EC%8A%A4%ED%84%B0-%EC%9D%B4%EB%8B%A4%EC%86%9C-%ED%92%80%EC%9D%B4
'''
import sys

n,m=map(int,sys.stdin.readline().rstrip().split())
pokemon={}
for i in range(n):
	a=sys.stdin.readline().rstrip()
	pokemon[a]=i+1
	pokemon[i+1]=a
for i in range(m):
	inp=sys.stdin.readline().rstrip()
	if inp.isdigit(): print(pokemon[int(inp)])
	else: print(pokemon[inp])
