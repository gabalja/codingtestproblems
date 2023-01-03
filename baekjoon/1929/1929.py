'''
소수 구하기 python 풀이
https://doctcoder.tistory.com/entry/%EC%86%8C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
def primes(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           
            for j in range(i+i, n, i): 
                sieve[j] = False
    return [i for i in range(2, n) if sieve[i] == True]

arr=primes(1000000)
a,b=map(int,input().split())
for i in range(len(arr)):
	if arr[i]>=a and arr[i]<=b: print(arr[i])
