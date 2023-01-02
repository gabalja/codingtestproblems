'''
분수찾기 python 풀이
https://doctcoder.tistory.com/entry/%EB%B6%84%EC%88%98%EC%B0%BE%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
x=int(input())
sum=0
cnt=0
while x>sum:
	cnt+=1
	sum+=cnt
if cnt%2==0:
	up=cnt
	down=1
	for i in range(sum-x):
		up-=1
		down+=1
else:
	up=1
	down=cnt
	for i in range(sum-x):
		up+=1
		down-=1
print(f'{up}/{down}')
