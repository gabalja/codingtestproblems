'''
종이 조각 python 풀이
https://doctcoder.tistory.com/entry/%EC%A2%85%EC%9D%B4-%EC%A1%B0%EA%B0%81-%ED%92%80%EC%9D%B4
'''
n,m=map(int,input().split())
inp=[list(map(int,input())) for i in range(n)]
def sol():
	res=0
	for i in range(1<<n*m):
		total=0
		for row in range(n):
			srow=0
			for col in range(m):
				idx=row*m+col
				if i&(1<<idx)!=0: srow=srow*10+inp[row][col]
				else:
					total+=srow
					srow=0
			total+=srow
		for col in range(m):
			scol=0
			for row in range(n):
				idx=row*m+col
				if i&(1<<idx)==0: scol=scol*10+inp[row][col]
				else:
					total+=scol
					scol=0
			total+=scol
		res=max(res,total)
	return res
print(sol())
