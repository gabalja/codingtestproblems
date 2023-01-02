'''
소수 python 풀이
https://doctcoder.tistory.com/entry/%EC%86%8C%EC%88%98-%ED%92%80%EC%9D%B4
'''
arr=[True]*10000
m=int(10000**0.5)
for i in range(2,m+1):
	if arr[i]==True:
		for j in range(i+i,10000,i):
			arr[j]=False
narr=[i for i in range(2,10000) if arr[i]==True]

narr.reverse()
m=int(input())
n=int(input())
sum=0
min=100000
for i in narr:
	if i<=n: 
		if i>=m:
			sum+=i
	if i>=m: min=i
if sum==0: print(-1)
else:
	print(sum)
	print(min)
