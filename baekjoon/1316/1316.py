'''
그룹 단어 체커 python 풀이
https://doctcoder.tistory.com/entry/%EA%B7%B8%EB%A3%B9-%EB%8B%A8%EC%96%B4-%EC%B2%B4%EC%BB%A4-%ED%92%80%EC%9D%B4
'''
n=int(input())
cnt=n
for i in range(n):
	word=input()
	for j in range(0,len(word)-1):
		if word[j]==word[j+1]: pass
		elif word[j] in word[j+1:]: 
			cnt-=1
			break
print(cnt)
