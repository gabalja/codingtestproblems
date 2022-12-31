'''
숫자의 합 python 풀이
https://doctcoder.tistory.com/entry/%EC%88%AB%EC%9E%90%EC%9D%98-%ED%95%A9-%ED%92%80%EC%9D%B4
'''
n=int(input())
num=input()
sum=0
for i in range(len(num)):
	sum+=int(num[i])
print(sum)
