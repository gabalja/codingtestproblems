'''
접미사 배열 python 풀이
https://doctcoder.tistory.com/entry/%EC%A0%91%EB%AF%B8%EC%82%AC-%EB%B0%B0%EC%97%B4-%ED%92%80%EC%9D%B4
'''
s=input()
res=[]
for i in range(len(s)):
	res.append(s[i:])
res.sort()
for i in res:
	print(i)
