'''
골드바흐의 추측 python 풀이
https://doctcoder.tistory.com/entry/%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90%EC%9D%98-%EC%B6%94%EC%B8%A1-%ED%92%80%EC%9D%B4
'''
def primes(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           
            for j in range(i+i, n, i): 
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

arr=primes(10000)
t=int(input())
for i in range(t):
	n=int(input())
	for j in range(int(n/2),n):
		if j in arr and n-j in arr:
			p2=j
			p1=n-j
			break
	print(p1,p2)
