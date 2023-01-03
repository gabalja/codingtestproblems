'''
최댓값 python 풀이
https://doctcoder.tistory.com/entry/%EC%B5%9C%EB%8C%93%EA%B0%92-%ED%92%80%EC%9D%B4-1
'''
mat=[]
matsize=9
for i in range(matsize):
	mat.append(list(map(int,input().split())))
max=-1
row=0
col=0
for i in range(matsize):
	for j in range(matsize):
		if mat[i][j]>max: 
			max=mat[i][j]
			row=i
			col=j
print(max)
print(row+1,col+1)
