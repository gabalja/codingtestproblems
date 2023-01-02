'''
설탕 배달 python 풀이
https://doctcoder.tistory.com/entry/%EC%84%A4%ED%83%95-%EB%B0%B0%EB%8B%AC-%ED%92%80%EC%9D%B4
'''
n=int(input())
three=0
five=int(n/5)
n%=5
while five>=0:
	if n%3==0:
		three=int(n/3)
		n%=3
		break
	five-=1
	n+=5
if n==0: print(five+three)
else: print(-1)
