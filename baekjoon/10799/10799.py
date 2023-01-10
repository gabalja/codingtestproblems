'''
쇠막대기 python 풀이
https://doctcoder.tistory.com/entry/%EC%87%A0%EB%A7%89%EB%8C%80%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
stack=[]
res=0
inp=list(input())
for i in range(len(inp)):
	if inp[i]=='(':
		stack.append('(')
	else:
		if inp[i-1]=='(':
			stack.pop()
			res+=len(stack)
		else:
			stack.pop()
			res+=1
print(res)
