'''
오븐 시계 python 풀이
https://doctcoder.tistory.com/entry/%EC%98%A4%EB%B8%90-%EC%8B%9C%EA%B3%84-%ED%92%80%EC%9D%B4
'''
a,b=map(int,input().split())
c=int(input())
b+=c
while(b>=60):
	b-=60
	a+=1
	if(a>=24): a-=24
print(a,b)
