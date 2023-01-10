'''
후위 표기식2 python 풀이
https://doctcoder.tistory.com/entry/%ED%9B%84%EC%9C%84-%ED%91%9C%EA%B8%B0%EC%8B%9D2-%ED%92%80%EC%9D%B4
'''
n=int(input())
inp=input()
nums=[int(input()) for i in range(n)]
stack=[]
for i in range(len(inp)):
	if inp[i].isalpha(): stack.append(nums[ord(inp[i])-65]) # 수 집어넣기
	else:
		a=stack.pop() # 수 계산
		calc=stack.pop()
		if inp[i]=='+': calc+=a
		elif inp[i]=='-': calc-=a
		elif inp[i]=='*': calc*=a
		elif inp[i]=='/': calc/=a
		stack.append(calc)
print("%.2f"%stack[0]) # 소수점 출력
