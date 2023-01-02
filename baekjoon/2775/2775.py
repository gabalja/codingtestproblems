'''
부녀회장이 될테야 python 풀이
https://doctcoder.tistory.com/entry/%EB%B6%80%EB%85%80%ED%9A%8C%EC%9E%A5%EC%9D%B4-%EB%90%A0%ED%85%8C%EC%95%BC-%ED%92%80%EC%9D%B4
'''
apt=[[0 for col in range(15)] for row in range(15)]
apt[0]=[x+1 for x in range(15)]
for i in range(1,15):
	for j in range(15):
		for k in range(j+1):
			apt[i][j]+=apt[i-1][k]
t=int(input())
for i in range(t):
	k=int(input())
	n=int(input())
	print(apt[k][n-1])
