'''
블랙잭 python 풀이
https://doctcoder.tistory.com/entry/%EB%B8%94%EB%9E%99%EC%9E%AD-%ED%92%80%EC%9D%B4
'''
n,m=map(int,input().split())
maxs=0
cards=list(map(int,input().split()))
for i in range(0,n-2):
	for j in range(i+1,n-1):
		for k in range(j+1,n):
			nmaxs=cards[i]+cards[j]+cards[k]
			if nmaxs<=m and maxs<nmaxs: maxs=nmaxs
print(maxs)
