'''
ACM 호텔 python 풀이
https://doctcoder.tistory.com/entry/ACM-%ED%98%B8%ED%85%94-%ED%92%80%EC%9D%B4
'''
t=int(input())
for i in range(t):
	h,w,n=map(int,input().split())
	floor=n%h
	room=int(n/h)+1
	if floor==0:
		floor=h
		room-=1
	if room>=10: print(f'{floor}{room}')
	else: print(f'{floor}0{room}')
