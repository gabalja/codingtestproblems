'''
수 이어 쓰기 1 python 풀이
https://doctcoder.tistory.com/entry/%EC%88%98-%EC%9D%B4%EC%96%B4-%EC%93%B0%EA%B8%B0-1-%ED%92%80%EC%9D%B4
'''
n=input()
inp=int(n)
res=len(n)*inp
for i in range(1,len(n)):
	res-=(10**i-1)
print(res)
