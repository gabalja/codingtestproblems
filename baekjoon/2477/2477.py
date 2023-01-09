'''
참외밭 python 풀이
https://doctcoder.tistory.com/entry/%EC%B0%B8%EC%99%B8%EB%B0%AD-%ED%92%80%EC%9D%B4
'''
k=int(input())
total=[]
x=[]
y=[]
small=[]
for i in range(6):
	dir,leng=map(int,input().split())
	if dir==3 or dir==4: x.append(leng)
	if dir==1 or dir==2: y.append(leng)
	total.append([dir,leng])
for i in range(6):
	if total[i][0]==total[(i+2)%6][0]:
		small.append(total[(i+1)%6][1])
print((max(x)*max(y)-small[0]*small[1])*k)
