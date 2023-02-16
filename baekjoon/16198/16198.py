'''
에너지 모으기 python 풀이
https://doctcoder.tistory.com/entry/%EC%97%90%EB%84%88%EC%A7%80-%EB%AA%A8%EC%9C%BC%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
def dfs(arr,tot):
	global res
	if len(arr)==2:
		res=max(res,tot)
		return
	for i in range(1,len(arr)-1):
		dfs(arr[:i]+arr[i+1:],tot+(arr[i-1]*arr[i+1]))
	
n=int(input())
nums=list(map(int,input().split()))
res=0
dfs(nums,res)
print(res)
