'''
리모컨 python 풀이
https://doctcoder.tistory.com/entry/%EB%A6%AC%EB%AA%A8%EC%BB%A8-%ED%92%80%EC%9D%B4
'''
n=int(input())
m=int(input())
arr={str(i) for i in range(10)}
if m!=0: arr-=set(input().split())
cnt=abs(100-n)
for i in range(1000000):
	i=str(i)
	for j in range(len(i)):
		if i[j] not in arr:
			break
		elif j==len(i)-1:
			cnt=min(cnt,abs(int(i)-n)+len(i))
print(cnt)
