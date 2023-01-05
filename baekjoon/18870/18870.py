'''
좌표 압축 python 풀이
https://doctcoder.tistory.com/entry/%EC%A2%8C%ED%91%9C-%EC%95%95%EC%B6%95-%ED%92%80%EC%9D%B4
'''
n=int(input())
cor=list(map(int,input().split()))
ncor=list(sorted(set(cor)))
dic={ncor[i]:i for i in range(len(ncor))}
for i in cor:
	print(dic[i],end=" ")
