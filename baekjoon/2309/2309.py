'''
일곱 난쟁이 python 풀이
https://doctcoder.tistory.com/entry/%EC%9D%BC%EA%B3%B1-%EB%82%9C%EC%9F%81%EC%9D%B4-%ED%92%80%EC%9D%B4
'''
arr=[]
hsum=0
for i in range(9):
	inp=int(input())
	arr.append(inp)
	hsum+=inp
arr.sort()
hsum-=100
check=True
for i in range(1,9):
	for j in range(0,i):
		if arr[i]+arr[j]==hsum:
			arr[i]*=0
			arr[j]*=0
			check=False
			break
	if check==False: break
for i in range(9):
	if arr[i]!=0:
		print(arr[i])
