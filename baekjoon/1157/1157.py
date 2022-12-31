'''
단어 공부 python 풀이
https://doctcoder.tistory.com/entry/%EB%8B%A8%EC%96%B4-%EA%B3%B5%EB%B6%80-%ED%92%80%EC%9D%B4
'''
inp=input().upper()
newinp=list(set(inp))
cnt=[]
for i in newinp:
	cnt.append(inp.count(i))
if(cnt.count(max(cnt))>1): print('?')
else: print(newinp[cnt.index(max(cnt))])
