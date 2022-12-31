'''
개수 세기 python 풀이
https://doctcoder.tistory.com/entry/%EA%B0%9C%EC%88%98-%EC%84%B8%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
n=int(input())
arr=list(map(int,input().split()))
cnt=0
v=int(input())
for i in arr:
	if(i==v): cnt+=1
print(cnt)
