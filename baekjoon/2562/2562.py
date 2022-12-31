'''
최댓값 python 풀이
https://doctcoder.tistory.com/entry/%EC%B5%9C%EB%8C%93%EA%B0%92-%ED%92%80%EC%9D%B4
'''
max=-1
idx=-1
for i in range(9):
	a=int(input())
	if(max<a):
		max=a
		idx=i+1
print(max)
print(idx)
