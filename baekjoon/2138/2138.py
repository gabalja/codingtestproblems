'''
전구와 스위치 python 풀이
https://doctcoder.tistory.com/entry/%EC%A0%84%EA%B5%AC%EC%99%80-%EC%8A%A4%EC%9C%84%EC%B9%98-%ED%92%80%EC%9D%B4
'''
n=int(input())
b=list(map(int, input()))
target=list(map(int, input()))
def change(A, B):
    L = A[:]
    press = 0
    for i in range(1, n):
        if L[i-1] == B[i-1]:
            continue
        press += 1
        for j in range(i-1, i+2):
            if j<n:
                L[j] = 1 - L[j]
    return press if L == B else 1e9
res=change(b, target)
b[0]=1-b[0]
b[1]=1-b[1]
res=min(res,change(b,target)+1)
print(res if res!=1e9 else-1)
