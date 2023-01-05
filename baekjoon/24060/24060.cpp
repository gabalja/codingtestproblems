/*
알고리즘 수업 - 병합 정렬 1 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%88%98%EC%97%85-%EB%B3%91%ED%95%A9-%EC%A0%95%EB%A0%AC-1-%ED%92%80%EC%9D%B4
*/
#include <iostream>
using namespace std;

int* A;
int* tmp;
int N, cnt = 0, K = 0, result = -1;

void merge(int A[], int p, int q, int r)
{
    int i = p, j = q + 1, t = 1;
  
    while (i <= q && j <= r)
    {
        if (A[i] <= A[j])
            tmp[t++] = A[i++];
        else
            tmp[t++] = A[j++];
    }
    while (i <= q) 
        tmp[t++] = A[i++];

    while (j <= r) 
        tmp[t++] = A[j++];

    i = p, t = 1;
    while (i <= r) 
    {
        A[i++] = tmp[t++];
        cnt++;
        if (cnt == K)
        {
            result = A[i - 1];
            break;
        }
    }
}

void merge_sort(int A[], int p, int r)
{
    if (p < r)
    {
        int q = (p + r) / 2;
        merge_sort(A, p, q);
        merge_sort(A, q + 1, r);
        merge(A, p, q, r);
    }
}

int main() {
    cin >> N >> K;
    A = new int[N + 1];
    tmp = new int[N + 1];
    for (int i = 0; i < N; i++)
        cin >> A[i];
    merge_sort(A, 0, N - 1);
    cout << result;
    delete[] A;
    delete[] tmp;
    return 0;
}
