'''
팩토리얼 0의 개수 python 풀이
https://doctcoder.tistory.com/entry/%ED%8C%A9%ED%86%A0%EB%A6%AC%EC%96%BC-0%EC%9D%98-%EA%B0%9C%EC%88%98-%ED%92%80%EC%9D%B4
'''
n=int(input())
fives=0
twos=0
while n>1:
	nn=n
	while nn%5==0 or nn%2==0:
		if nn%5==0:
			fives+=1
			nn=nn//5
		if nn%2==0:
			twos+=1
			nn=nn//2
	n-=1
print(min(fives,twos))
