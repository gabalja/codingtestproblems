'''
대칭 차집합 python 풀이
https://doctcoder.tistory.com/entry/%EB%8C%80%EC%B9%AD-%EC%B0%A8%EC%A7%91%ED%95%A9-%ED%92%80%EC%9D%B4
'''
n,m=map(int,input().split())
sn=set(map(int,input().split()))
sm=set(map(int,input().split()))
print(len(sn-sm)+len(sm-sn))
