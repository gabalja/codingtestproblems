'''
단어 수학 python 풀이
https://doctcoder.tistory.com/entry/%EB%8B%A8%EC%96%B4-%EC%88%98%ED%95%99-%ED%92%80%EC%9D%B4
'''
n=int(input())
alpha=[0 for i in range(26)]
for i in range(n):
	inp=input().rstrip()
	for j in range(len(inp)):
		alpha[ord(inp[j])-ord('A')]+=10**(len(inp)-j-1)
alpha.sort()
res=0
num=9
for i in range(25,0,-1):
	if alpha[i]==0 or num<1:
		break
	res+=alpha[i]*num
	num-=1
print(res)
