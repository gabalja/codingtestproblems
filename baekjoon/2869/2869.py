'''
달팽이는 올라가고 싶다 python 풀이
https://doctcoder.tistory.com/entry/%EB%8B%AC%ED%8C%BD%EC%9D%B4%EB%8A%94-%EC%98%AC%EB%9D%BC%EA%B0%80%EA%B3%A0-%EC%8B%B6%EB%8B%A4-%ED%92%80%EC%9D%B4
'''
a,b,v=map(int,input().split())
day=int((v-a)/(a-b))+1
if (v-a)%(a-b)!=0: day+=1
print(day)
