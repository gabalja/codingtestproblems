'''
수 정렬하기 python 풀이
https://doctcoder.tistory.com/entry/%EC%88%98-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
n=int(input())
arr=[]
for _ in range(n):
	arr.append(int(input()))
for i in range(1,n):
	for j in range(i,0,-1):
		if arr[j-1]>arr[j]:
			arr[j-1],arr[j]=arr[j],arr[j-1]
for i in range(n):
	print(arr[i])
