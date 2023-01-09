'''
직사각형에서 탈출 python 풀이
https://doctcoder.tistory.com/entry/%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95%EC%97%90%EC%84%9C-%ED%83%88%EC%B6%9C-%ED%92%80%EC%9D%B4
'''
x,y,w,h=map(int,input().split())
min=10000
for i in range(4):
	if min>x: min=x
	if min>y: min=y
	if min>w-x: min=w-x
	if min>h-y: min=h-y
print(min)
