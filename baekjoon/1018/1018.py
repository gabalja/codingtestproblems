'''
체스판 다시 칠하기 python 풀이
https://doctcoder.tistory.com/entry/%EC%B2%B4%EC%8A%A4%ED%8C%90-%EB%8B%A4%EC%8B%9C-%EC%B9%A0%ED%95%98%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
n,m=map(int,input().split())
board=[]
check=[]
for i in range(n):
	board.append(input())
for a in range(n-7):
	for b in range(m-7):
		white=0
		black=0
		for i in range(a,a+8):
			for j in range(b,b+8):
				if (i+j)%2==0:
					if board[i][j]!='W':
						white+=1
					if board[i][j]!='B':
						black+=1
				else:
					if board[i][j]!='B':
						white+=1
					if board[i][j]!='W':
						black+=1
		check.append(min(white,black))
print(min(check))
