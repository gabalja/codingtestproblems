'''
크로아티아 알파벳 python 풀이
https://doctcoder.tistory.com/entry/%ED%81%AC%EB%A1%9C%EC%95%84%ED%8B%B0%EC%95%84-%EC%95%8C%ED%8C%8C%EB%B2%B3-%ED%92%80%EC%9D%B4
'''
calpha=["c=","c-","dz=","d-","lj","nj","s=","z="]
inp=input()
for i in calpha:
	inp=inp.replace(i,' ')
print(len(inp))
