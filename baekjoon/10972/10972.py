'''
다음 순열 python 풀이
https://doctcoder.tistory.com/entry/%EB%8B%A4%EC%9D%8C-%EC%88%9C%EC%97%B4-%ED%92%80%EC%9D%B4
'''
N=int(input())
arr=list(map(int, input().split()))

def next_permutation():
    i=N-1
    while(i>0 and arr[i-1]>=arr[i]):
        i-=1
    if i==0:
        return False
    j=N-1
    while(arr[i-1]>=arr[j]):
        j-=1
    arr[i-1], arr[j] = arr[j], arr[i-1]
    k=N-1
    while(i<k):
        arr[i], arr[k] = arr[k], arr[i]
        i+=1
        k-=1
    return True

if not next_permutation():
    print(-1)
else:
    for i in range(N):
        print(arr[i], end=" ")
