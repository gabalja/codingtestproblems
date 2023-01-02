'''
벌집 python 풀이
https://doctcoder.tistory.com/entry/%EB%B2%8C%EC%A7%91-%ED%92%80%EC%9D%B4
'''
n=int(input())
i=1
room=1
while n>room:
	i+=1
	room+=(6*(i-1))
print(i)
