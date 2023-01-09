'''
이항 계수 1 python 풀이
https://doctcoder.tistory.com/entry/%EC%9D%B4%ED%95%AD-%EA%B3%84%EC%88%98-1-%ED%92%80%EC%9D%B4
'''
def fac(i):
	if i==1 or i==0: return 1
	else: return i*fac(i-1)

a,b=map(int,input().split())
res=fac(a)//fac(b)//fac(a-b)
print(res)
