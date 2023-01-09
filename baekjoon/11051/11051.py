'''
이항 계수 2 python 풀이
https://doctcoder.tistory.com/entry/%EC%9D%B4%ED%95%AD-%EA%B3%84%EC%88%98-2-%ED%92%80%EC%9D%B4
'''
n,k=map(int,input().split())
over=1
for i in range(k):
	over*=n
	n-=1
under=1
for i in range(2,k+1):
	under*=i
print((over//under)%10007)
