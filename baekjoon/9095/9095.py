'''
1, 2, 3 더하기 python 풀이
https://doctcoder.tistory.com/entry/1-2-3-%EB%8D%94%ED%95%98%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
arr=[0]*12
arr[1]=1
arr[2]=2
arr[3]=4
for i in range(4,12):
	arr[i]=arr[i-1]+arr[i-2]+arr[i-3]
t=int(input())
for i in range(t):
	print(arr[int(input())])
