'''
동전 0 python 풀이
https://doctcoder.tistory.com/entry/%EB%8F%99%EC%A0%84-0-%ED%92%80%EC%9D%B4
'''
n,k=map(int,input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)
answer = 0
for coin in coins:
    if k >= coin:
        answer += k // coin
        k %= coin
        if k <= 0:
       		break
print(answer)
