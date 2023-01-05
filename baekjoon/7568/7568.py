'''
덩치 python 풀이
https://doctcoder.tistory.com/entry/%EB%8D%A9%EC%B9%98-%ED%92%80%EC%9D%B4
'''
n=int(input())
x=[]
y=[]
rec=[1 for i in range(n)]
for i in range(n):
	a,b=map(int,input().split())
	x.append(a)
	y.append(b)
for i in range(n):
	for j in range(n):
		if x[i]>x[j] and y[i]>y[j]:
			rec[j]+=1
for i in range(n):
	print(rec[i],end=" ")
