'''
영화감독 숌 python 풀이
https://doctcoder.tistory.com/entry/%EC%98%81%ED%99%94%EA%B0%90%EB%8F%85-%EC%88%8C-%ED%92%80%EC%9D%B4
'''
n=int(input())
cnt=0
num=666
while cnt<n:
	i=num
	while i>0:
		if i%1000==666:
			cnt+=1
			break
		i=i//10
	num+=1
print(num-1)
