'''
최대공약수와 최소공배수 python 풀이
https://doctcoder.tistory.com/entry/%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%99%80-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98-%ED%92%80%EC%9D%B4
'''
def gcd(a,b):
	if b==0: return a
	else: return gcd(b,a%b)

a,b=map(int,input().split())
x=gcd(a,b)
print(x)
print(int(a*b/x))
