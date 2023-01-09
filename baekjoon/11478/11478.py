'''
서로 다른 부분 문자열의 개수 python 풀이
https://doctcoder.tistory.com/entry/%EC%84%9C%EB%A1%9C-%EB%8B%A4%EB%A5%B8-%EB%B6%80%EB%B6%84-%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%98-%EA%B0%9C%EC%88%98-%ED%92%80%EC%9D%B4
'''
s=input()
result=set()
for i in range(len(s)):
	for j in range(i,len(s)):
		result.add(s[i:j+1])
print(len(result))
