'''
날짜 계산 python 풀이
https://doctcoder.tistory.com/entry/%EB%82%A0%EC%A7%9C-%EA%B3%84%EC%82%B0-%ED%92%80%EC%9D%B4
'''
e,s,m=map(int,input().split())
year=1
while True:
	anse=year%15
	if anse==0: anse=15
	anss=year%28
	if anss==0: anss=28
	ansm=year%19
	if ansm==0: ansm=19
	if anse==e and anss==s and ansm==m: break
	year+=1
print(year)
