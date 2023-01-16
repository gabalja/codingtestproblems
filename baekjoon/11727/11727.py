'''
2×n 타일링 2 python 풀이
https://doctcoder.tistory.com/entry/2%C3%97n-%ED%83%80%EC%9D%BC%EB%A7%81-2-%ED%92%80%EC%9D%B4
'''
n=int(input())
arr=[0 for i in range(1001)]
arr[1]=1
arr[2]=3
for i in range(3,1001):
	arr[i]=arr[i-1]+arr[i-2]*2
print(arr[n]%10007)
