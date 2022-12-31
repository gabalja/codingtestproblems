'''
한수 python 풀이
https://doctcoder.tistory.com/entry/%ED%95%9C%EC%88%98-%ED%92%80%EC%9D%B4
'''
def han(n):
	if(n<100): res=1
	elif((int(n/100)-(int(n/10)%10))==((int(n/10)%10)-(n%10))): res=1
	else: res=0
	return res

n=int(input())
cnt=0
for i in range(1,n+1):
	if(han(i)==1): cnt+=1
print(cnt)
