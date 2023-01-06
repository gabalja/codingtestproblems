'''
숫자 카드 python 풀이
https://doctcoder.tistory.com/entry/%EC%88%AB%EC%9E%90-%EC%B9%B4%EB%93%9C-%ED%92%80%EC%9D%B4
'''
def bisearch(arr,target,start,end):
	while start<=end:
		mid=(start+end)//2
		if arr[mid]==target:
			return mid
		elif arr[mid]>target:
			end=mid-1
		else: start=mid+1
	return False

n=int(input())
card=list(map(int,input().split()))
m=int(input())
num=list(map(int,input().split()))
card.sort()
for i in range(m):
	if bisearch(card,num[i],0,n-1) is not False: print(1,end=' ')
	else: print(0,end=' ')
