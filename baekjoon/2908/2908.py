'''
상수 python 풀이
https://doctcoder.tistory.com/entry/%EC%83%81%EC%88%98-%ED%92%80%EC%9D%B4
'''
a,b=map(int,input().split())
na=(a%10)*100+(int(a/10)%10)*10+int(a/100)
nb=(b%10)*100+(int(b/10)%10)*10+int(b/100)
print(na if na>nb else nb)
