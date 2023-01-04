'''
소트인사이드 python 풀이
https://doctcoder.tistory.com/entry/%EC%86%8C%ED%8A%B8%EC%9D%B8%EC%82%AC%EC%9D%B4%EB%93%9C-%ED%92%80%EC%9D%B4
'''
n=input()
arr=[]
for i in n:
	arr.append(int(i))
arr.sort()
arr.reverse()
for i in arr:
	print(i,end='')
