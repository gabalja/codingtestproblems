'''
더하기 사이클 python 풀이
https://doctcoder.tistory.com/entry/%EB%8D%94%ED%95%98%EA%B8%B0-%EC%82%AC%EC%9D%B4%ED%81%B4-%ED%92%80%EC%9D%B4
'''
n=int(input())
nn=n
cycle=0
while 1:
	nn=(nn%10)*10+(int(nn/10)+(nn%10))%10
	cycle+=1
	if(nn==n): break
print(cycle)
