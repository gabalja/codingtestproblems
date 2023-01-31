'''
부등호 python 풀이
https://doctcoder.tistory.com/entry/%EB%B6%80%EB%93%B1%ED%98%B8-%ED%92%80%EC%9D%B4
'''
def check(a,b,c):
	if c=='<': return a<b
	else: return a>b

def res(depth,s):
	global maxs,mins
	if depth==k+1:
		if len(mins)==0: mins=s
		else: maxs=s
		return
	for i in range(10):
		if not visit[i]:
			if depth==0 or check(s[-1],str(i),arr[depth-1]):
				visit[i]=True
				res(depth+1,s+str(i))
				visit[i]=False

k=int(input())
arr=list(input().split())
visit=[0]*10
maxs=""
mins=""
res(0,"")
print(maxs)
print(mins)
