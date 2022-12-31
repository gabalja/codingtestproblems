'''
최소, 최대 python 풀이
https://doctcoder.tistory.com/entry/%EC%B5%9C%EC%86%8C-%EC%B5%9C%EB%8C%80-%ED%92%80%EC%9D%B4
'''
n=int(input())
arr=list(map(int,input().split()))
max=-2000000
min=2000000
for i in arr:
	if(i<min): min=i
	if(i>max): max=i
print(min,max)
