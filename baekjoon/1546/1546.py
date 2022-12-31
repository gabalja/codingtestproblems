'''
평균 python 풀이
https://doctcoder.tistory.com/entry/%ED%8F%89%EA%B7%A0-%ED%92%80%EC%9D%B4
'''
n=int(input())
score=list(map(int,input().split()))
score.sort()
m=score[-1]
sum=0
for i in score:
	i=i/m*100
	sum+=i
print(sum/n)
