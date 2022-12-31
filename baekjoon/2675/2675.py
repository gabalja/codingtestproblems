'''
문자열 반복 python 풀이
https://doctcoder.tistory.com/entry/%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%B0%98%EB%B3%B5-%ED%92%80%EC%9D%B4
'''
t=int(input())
for k in range(t):
	r,s=input().split()
	r=int(r)
	for i in range(len(s)):
		for j in range(r):
			print(s[i],end='')
	print('')
