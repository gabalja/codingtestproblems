'''
알파벳 찾기 python 풀이
https://doctcoder.tistory.com/entry/%EC%95%8C%ED%8C%8C%EB%B2%B3-%EC%B0%BE%EA%B8%B0-%ED%92%80%EC%9D%B4
'''
inp=input()
alpha="abcdefghijklmnopqrstuvwxyz"
for i in range(len(alpha)):
	print(inp.find(alpha[i]),end=' ')
