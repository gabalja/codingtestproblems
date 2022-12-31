'''
셀프 넘버 python 풀이
https://doctcoder.tistory.com/entry/%EC%85%80%ED%94%84-%EB%84%98%EB%B2%84-%ED%92%80%EC%9D%B4
'''
def selfnum(n):
	sum=n
	while(n!=0):
		sum+=n%10
		n=int(n/10)
	return sum

arr=[i+1 for i in range(10000)]
for i in range(1,10000):
	check=selfnum(i)
	if(check in arr): arr.remove(check)
for i in range(len(arr)):
	print(arr[i])
