'''
별 찍기 - 1 python 풀이
https://doctcoder.tistory.com/entry/%EB%B3%84-%EC%B0%8D%EA%B8%B0-1-%ED%92%80%EC%9D%B4
'''
n=int(input())
for i in range(n):
	for j in range(i+1):
		print('*',end='') 
	print('')
