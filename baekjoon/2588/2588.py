'''
곱셈 python 풀이
https://doctcoder.tistory.com/entry/%EA%B3%B1%EC%85%88-%ED%92%80%EC%9D%B4
'''
a=int(input())
b=int(input())
print(a*(b%10))
print(a*(int(b/10)%10))
print(a*int(b/100))
print(a*b)
