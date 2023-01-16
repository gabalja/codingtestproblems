'''
Base Conversion python 풀이
https://doctcoder.tistory.com/entry/Base-Conversion-%ED%92%80%EC%9D%B4
'''
a,b=map(int,input().split())
m=int(input())
arr=list(map(int,input().split()))[::-1]
tens=0
for i in range(len(arr)):
	tens+=arr[i]*(a**i)
res=[]
while tens:
	res.append(tens%b)
	tens//=b
print(*reversed(res))
