'''
커트라인 python 풀이
https://doctcoder.tistory.com/entry/%EC%BB%A4%ED%8A%B8%EB%9D%BC%EC%9D%B8-%ED%92%80%EC%9D%B4
'''
n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
print(arr[-k])
