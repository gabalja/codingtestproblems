'''
약수 python 풀이
https://doctcoder.tistory.com/entry/%EC%95%BD%EC%88%98-%ED%92%80%EC%9D%B4
'''
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
print(arr[0]*arr[-1])
