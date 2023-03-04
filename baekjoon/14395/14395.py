'''
A+B python 풀이
https://doctcoder.tistory.com/entry/AB-%ED%92%80%EC%9D%B4
'''
import collections
import math

s,t = map(int,input().split())
if s == t:
    print(0)
elif t == 1:
    print('/')
else:
    visited = set()
    q = collections.deque()
    q.append((s, ''))
    while q:
        tmp, tmp_method = q.popleft()
        if tmp == t:
            print(tmp_method)
            break
        else:
            if tmp * tmp <= 10**9 and tmp * tmp not in visited:
                q.append((tmp * tmp, tmp_method + '*'))
                visited.add(tmp * tmp)
            if tmp + tmp <= 10**9 and tmp + tmp not in visited:
                q.append((tmp + tmp, tmp_method + '+'))
                visited.add(tmp + tmp)
            if tmp / tmp not in visited:
                q.append((tmp / tmp, tmp_method + '/'))
                visited.add(1)
    else:
        print(-1)
