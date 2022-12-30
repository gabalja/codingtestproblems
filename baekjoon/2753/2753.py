'''
윤년 python 풀이
https://doctcoder.tistory.com/entry/%EC%9C%A4%EB%85%84-%ED%92%80%EC%9D%B4
'''
year=int(input())
if(year%4==0):
	if(year%400==0): print(1)
	elif(year%100!=0): print(1)
	else: print(0)
else: print(0)
