'''
회의실 배정 python 풀이
https://doctcoder.tistory.com/entry/%ED%9A%8C%EC%9D%98%EC%8B%A4-%EB%B0%B0%EC%A0%95-%ED%92%80%EC%9D%B4
'''
n=int(input())
time=[]
for _ in range(n):
  st,end=map(int,input().split())
  time.append([st,end])
time = sorted(time, key=lambda a: a[0]) 
time = sorted(time, key=lambda a: a[1])
last = 0 
conut = 0 
for i, j in time:
  if i >= last:
    conut += 1
    last = j
print(conut)
