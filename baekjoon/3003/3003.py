'''
킹, 퀸, 룩, 비숍, 나이트, 폰 python 풀이
https://doctcoder.tistory.com/entry/%ED%82%B9-%ED%80%B8-%EB%A3%A9-%EB%B9%84%EC%88%8D-%EB%82%98%EC%9D%B4%ED%8A%B8-%ED%8F%B0-%ED%92%80%EC%9D%B4
'''
chess=[1,1,2,2,2,8]
inp=list(map(int,input().split()))
for i in range(len(chess)):
	chess[i]-=inp[i]
	print(chess[i],end=' ')
