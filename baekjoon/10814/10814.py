'''
나이순 정렬 python 풀이
https://doctcoder.tistory.com/entry/%EB%82%98%EC%9D%B4%EC%88%9C-%EC%A0%95%EB%A0%AC-%ED%92%80%EC%9D%B4
'''
n=int(input())
user=[]
for i in range(n):
	age,name=input().split()
	age=int(age)
	idx=i
	user.append([age,name,idx])
user.sort(key=lambda x:(x[0],x[2]))
for i in user: print(i[0],i[1])
