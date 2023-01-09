'''
네 번째 점 python 풀이
https://doctcoder.tistory.com/entry/%EB%84%A4-%EB%B2%88%EC%A7%B8-%EC%A0%90-%ED%92%80%EC%9D%B4
'''
x=[]
y=[]
resx=0
resy=0
for i in range(3):
	a,b=map(int,input().split())
	x.append(a)
	y.append(b)
if x[0]==x[1]: resx=x[2]
elif x[0]==x[2]: resx=x[1]
else: resx=x[0]
if y[0]==y[1]: resy=y[2]
elif y[0]==y[2]: resy=y[1]
else: resy=y[0]
print(resx,resy)
