'''
손익분기점 python 풀이
https://doctcoder.tistory.com/entry/%EC%86%90%EC%9D%B5%EB%B6%84%EA%B8%B0%EC%A0%90-%ED%92%80%EC%9D%B4
'''
a,b,c=map(int,input().split())
if b>=c: res=-1
else: res=int(a/(c-b))+1
print(res)
