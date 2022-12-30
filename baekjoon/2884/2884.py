'''
알람 시계 python 풀이
https://doctcoder.tistory.com/entry/%EC%95%8C%EB%9E%8C-%EC%8B%9C%EA%B3%84-%ED%92%80%EC%9D%B4
'''
h,m=map(int,input().split())
if(m<45):
	h-=1
	m+=60
if(h<0): h+=24
print(h,m-45)
