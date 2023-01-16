'''
카드 구매하기 python 풀이
https://doctcoder.tistory.com/entry/%EC%B9%B4%EB%93%9C-%EA%B5%AC%EB%A7%A4%ED%95%98%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
n=int(input())
inp=[0]+list(map(int,input().split()))
arr=[0]*(n+1)
for i in range(1,n+1):
	for j in range(1,i+1):
		arr[i]=max(arr[i],arr[i-j]+inp[j])
print(arr[-1])
