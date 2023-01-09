'''
어린 왕자 python 풀이
https://doctcoder.tistory.com/entry/%EC%96%B4%EB%A6%B0-%EC%99%95%EC%9E%90-%ED%92%80%EC%9D%B4
'''
t=int(input())
for i in range(t):
	x1,y1,x2,y2=map(int,input().split())
	n=int(input())
	x=[]
	y=[]
	r=[]
	cnt=0
	for j in range(n):
		cx,cy,cr=map(int,input().split())
		x.append(cx)
		y.append(cy)
		r.append(cr)
	for j in range(n):
		stadis=((x1-x[j])**2+(y1-y[j])**2)**0.5
		enddis=((x2-x[j])**2+(y2-y[j])**2)**0.5
		rad=r[j]
		if stadis<rad:
			if rad<enddis: cnt+=1
		elif rad>enddis: cnt+=1
	print(cnt)
