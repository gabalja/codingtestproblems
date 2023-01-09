'''
조합 0의 개수 python 풀이
https://doctcoder.tistory.com/entry/%EC%A1%B0%ED%95%A9-0%EC%9D%98-%EA%B0%9C%EC%88%98-%ED%92%80%EC%9D%B4
'''
def count(a,b):
	cnt=0
	while a:
		a//=b
		cnt+=a
	return cnt

n,m=map(int,input().split())
fives=count(n,5)-count(m,5)-count(n-m,5)
twos=count(n,2)-count(m,2)-count(n-m,2)
print(min(fives,twos))
