'''
터렛 python 풀이
https://doctcoder.tistory.com/entry/%ED%84%B0%EB%A0%9B-%ED%92%80%EC%9D%B4
'''
t=int(input())
for i in range(t):
	x1,y1,r1,x2,y2,r2=map(int,input().split())
	dis=((x1-x2)**2+(y1-y2)**2)**0.5
	rsum=r1+r2
	rsub= r1-r2 if r1>r2 else r2-r1
	cnt=0
	if dis!=0:
		if rsum==dis: cnt+=1
		elif rsub==dis: cnt+=1
		elif rsum<dis or dis<rsub: cnt+=0
		else: cnt+=2
	else:
		if r1==r2: 
			print(-1)
			continue
	print(cnt)
