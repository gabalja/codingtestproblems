'''
대표값2 python 풀이
https://doctcoder.tistory.com/entry/%EB%8C%80%ED%91%9C%EA%B0%922-%ED%92%80%EC%9D%B4
'''
arr=[]
sum=0
for i in range(5):
	inp=int(input())
	arr.append(inp)
	sum+=inp
arr.sort()
print(int(sum/5))
print(arr[2])
