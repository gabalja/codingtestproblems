'''
스택 수열 python 풀이
https://doctcoder.tistory.com/entry/%EC%8A%A4%ED%83%9D-%EC%88%98%EC%97%B4-%ED%92%80%EC%9D%B4
'''
n=int(input())
stack=[]
res=[]
num=1
tf=True
for i in range(n):
	inp=int(input())
	while num<=inp:
		stack.append(num)
		res.append('+')
		num+=1
	if stack[-1]==inp:
		stack.pop()
		res.append('-')
	else:
		print("NO")
		tf=False
		break
if tf:
	for i in res:
		print(i)
