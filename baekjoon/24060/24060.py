'''
알고리즘 수업 - 병합 정렬 1 python 풀이
https://doctcoder.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%88%98%EC%97%85-%EB%B3%91%ED%95%A9-%EC%A0%95%EB%A0%AC-1-%ED%92%80%EC%9D%B4
'''
def mergeSort(L):
    if len(L) == 1:
        return L
    mid = (len(L) + 1)//2
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])
    L2 = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L2.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            L2.append(right[j])
            ans.append(right[j])
            j += 1
    while i < len(left):
        L2.append(left[i])
        ans.append(left[i])
        i += 1  
    while j < len(right):
        L2.append(right[j])
        ans.append(right[j])
        j += 1  
    return L2

n, k = map(int,input().split())
a = list(map(int,input().split()))
ans = []
mergeSort(a)
if len(ans) >= k: print(ans[k-1])
else: print(-1) 
