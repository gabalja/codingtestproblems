'''
ROT13 python 풀이
https://doctcoder.tistory.com/entry/ROT13-%ED%92%80%EC%9D%B4
'''
inp=input()
res=""
for i in inp:
	if i.isupper():
		a=ord(i)+13
		if a>90: a-=26
		res+=chr(a)
	elif i.islower():
		a=ord(i)+13
		if a>122: a-=26
		res+=chr(a)
	else: res+=i
print(res)
