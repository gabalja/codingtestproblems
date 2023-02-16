'''
연산자 끼워넣기 python 풀이
https://doctcoder.tistory.com/entry/%EC%97%B0%EC%82%B0%EC%9E%90-%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
def dfs(dep,tot,pl,mi,mu,di):
	global maxs,mins
	if dep==n:
		maxs=max(tot,maxs)
		mins=min(tot,mins)
		return
	if pl:
		dfs(dep+1,tot+nums[dep],pl-1,mi,mu,di)
	if mi:
		dfs(dep+1,tot-nums[dep],pl,mi-1,mu,di)
	if mu:
		dfs(dep+1,tot*nums[dep],pl,mi,mu-1,di)
	if di:
		dfs(dep+1,int(tot/nums[dep]),pl,mi,mu,di-1)

n=int(input())
nums=list(map(int,input().split()))
p,s,m,d=map(int,input().split())
maxs=-1e9
mins=1e9
dfs(1,nums[0],p,s,m,d)
print(maxs)
print(mins)
