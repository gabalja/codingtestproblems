/*
정수 N개의 합 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%A0%95%EC%88%98-N%EA%B0%9C%EC%9D%98-%ED%95%A9-%ED%92%80%EC%9D%B4
*/
#include <vector>
long long sum(std::vector<int> &a) {
	long long ans = 0;
    for(int i=0;i<a.size();i++)
    {
        ans+=a[i];
    }
    return ans;
}
