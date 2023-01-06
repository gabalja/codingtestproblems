'''
듣보잡 python 풀이
https://doctcoder.tistory.com/entry/%EB%93%A3%EB%B3%B4%EC%9E%A1-%ED%92%80%EC%9D%B4
'''
n,m=map(int,input().split())
name={input() for i in range(n)}
res=[]
for i in range(m):
	a=input()
	if a in name: res.append(a)
res.sort()
print(len(res))
for i in range(len(res)):
	print(res[i])
