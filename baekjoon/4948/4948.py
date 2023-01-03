'''
베르트랑 공준 python 풀이
https://doctcoder.tistory.com/entry/%EB%B2%A0%EB%A5%B4%ED%8A%B8%EB%9E%91-%EA%B3%B5%EC%A4%80-%ED%92%80%EC%9D%B4
'''
def primes(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           
            for j in range(i+i, n, i): 
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

arr=primes(300000)
while 1:
	n=int(input())
	if n==0: break
	cnt=0
	for i in arr:
		if n<i and i<=2*n: cnt+=1
	print(cnt)
