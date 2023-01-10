'''
골드바흐의 추측 python 풀이
https://doctcoder.tistory.com/entry/%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90%EC%9D%98-%EC%B6%94%EC%B8%A1-%ED%92%80%EC%9D%B4-1
'''
import sys

def primes(n):
	sieve = [True] * n
	m = int(n ** 0.5)
	for i in range(2, m + 1):
		if sieve[i] == True:           
			for j in range(i+i, n, i): 
				sieve[j] = False
	return {i:sieve[i] for i in range(n)}

arr=primes(1000000)
while 1:
	s=int(sys.stdin.readline().rstrip())
	if s==0: break
	a=3
	b=s-3
	for i in range(1000000):
		if arr[a] and arr[b]:
			print(f'{s} = {a} + {b}')
			break
		a+=1
		b-=1
	else:
		print("Goldbach's conjecture is wrong.")
