'''
팩토리얼 python 풀이
https://doctcoder.tistory.com/entry/%ED%8C%A9%ED%86%A0%EB%A6%AC%EC%96%BC-%ED%92%80%EC%9D%B4
'''
def fac(a):
	if a==1 or a==0: return 1
	return a*fac(a-1)

n=int(input())
print(fac(n))
