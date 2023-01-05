'''
별 찍기 - 10 python 풀이
https://doctcoder.tistory.com/entry/%EB%B3%84-%EC%B0%8D%EA%B8%B0-10-%ED%92%80%EC%9D%B4
'''
import sys
input = sys.stdin.readline
print = sys.stdout.write

def star(a,b,c):
	if a//c%3==1 and b//c%3==1:
		print(" ")
	else: 
		if c//3==0: print("*")
		else: star(a,b,c//3)

n=int(input())
for i in range(n):
	for j in range(n):
		star(i,j,n)
	print("\n")
