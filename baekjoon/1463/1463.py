'''
1로 만들기 python 풀이
https://doctcoder.tistory.com/entry/1%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
n=int(input())
arr=[0 for i in range(n+1)]
for i in range(2,n+1):
	arr[i]=arr[i-1]+1
	if i%2==0: arr[i]=min(arr[i],arr[i//2]+1)
	if i%3==0: arr[i]=min(arr[i],arr[i//3]+1)
print(arr[n])
