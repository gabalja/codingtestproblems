'''
문자열 분석 python 풀이
https://doctcoder.tistory.com/entry/%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%B6%84%EC%84%9D-%ED%92%80%EC%9D%B4
'''
while 1:
	try:
		inp=input()
		small=0
		big=0
		num=0
		space=0
		for i in inp:
			if i.isdigit(): num+=1
			elif i.islower(): small+=1
			elif i.isupper(): big+=1
			elif i.isspace(): space+=1
		print(small,big,num,space)
	except:
		break
