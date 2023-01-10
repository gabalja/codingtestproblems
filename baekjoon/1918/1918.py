'''
후위 표기식 python 풀이
https://doctcoder.tistory.com/entry/%ED%9B%84%EC%9C%84-%ED%91%9C%EA%B8%B0%EC%8B%9D-%ED%92%80%EC%9D%B4
'''
inp=input()
stack=[]
res=""
for i in inp:
	if i.isalpha(): res+=i
	else:
		if i=='(':
			stack.append(i)
		elif i=='*' or i=='/':
			while stack and (stack[-1]=='*'or stack[-1]=='/'):
				res+=stack.pop()
			stack.append(i)
		elif i=='+' or i=='-':
			while stack and stack[-1]!='(':
				res+=stack.pop()
			stack.append(i)
		elif i==')':
			while stack and stack[-1]!='(':
				res+=stack.pop()
			stack.pop()
while stack:
	res+=stack.pop()
print(res)
