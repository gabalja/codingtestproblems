'''
나머지 python 풀이
https://doctcoder.tistory.com/entry/%EB%82%98%EB%A8%B8%EC%A7%80-%ED%92%80%EC%9D%B4-1
'''
rem=[i for i in range(42)]
for i in range(10):
	a=int(input())%42
	if(a in rem): rem.remove(a)
print(42-len(rem))
