'''
색종이 python 풀이
https://doctcoder.tistory.com/entry/%EC%83%89%EC%A2%85%EC%9D%B4-%ED%92%80%EC%9D%B4
'''
num=int(input())
area=[[0 for i in range(101)] for j in range(101)]
for i in range(num):
	x,y=map(int,input().split())
	for j in range(x,x+10):
		for k in range(y,y+10):
			area[j][k]=1
res=0
for x in area:
	res+=x.count(1)
print(res)
