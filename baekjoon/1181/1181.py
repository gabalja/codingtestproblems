'''
단어 정렬 python 풀이
https://doctcoder.tistory.com/entry/%EB%8B%A8%EC%96%B4-%EC%A0%95%EB%A0%AC-%ED%92%80%EC%9D%B4
'''
n=int(input())
lists=set() # 중복 제거
for i in range(n):
	lists.add(input())
lists=list(lists)
lists.sort() # 사전순 정렬
lists.sort(key=lambda x:len(x)) # 길이순 정렬
for i in lists: print(i)
