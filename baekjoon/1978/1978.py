'''
소수 찾기 python 풀이
https://doctcoder.tistory.com/entry/%EC%86%8C%EC%88%98-%EC%B0%BE%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
arr=[True]*1000
m=int(1000**0.5)
for i in range(2,m+1):
	if arr[i]==True:
		for j in range(i+i,1000,i):
			arr[j]=False
narr=[i for i in range(2,1000) if arr[i]==True]
n=int(input())
nums=list(map(int,input().split()))
cnt=0
for i in range(n):
	if nums[i] in narr: cnt+=1
print(cnt)
