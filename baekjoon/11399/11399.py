'''
ATM python 풀이
https://doctcoder.tistory.com/entry/ATM-%ED%92%80%EC%9D%B4
'''
n=int(input())
p=list(map(int,input().split()))
p.sort()
answer=0
for x in range(1,n+1):
    answer += sum(p[0:x])
print(answer)
