'''
좌표 정렬하기 python 풀이
https://doctcoder.tistory.com/entry/%EC%A2%8C%ED%91%9C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
n=int(input())
cor=[]
for i in range(n):
	xy=list(map(int,input().split()))
	cor.append(xy)
cor.sort()
for i in range(n):
	print(cor[i][0],cor[i][1])
