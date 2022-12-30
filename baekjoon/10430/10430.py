'''
나머지 python 풀이
https://doctcoder.tistory.com/entry/%EB%82%98%EB%A8%B8%EC%A7%80-%ED%92%80%EC%9D%B4
'''
A,B,C=map(int,input().split())
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)
