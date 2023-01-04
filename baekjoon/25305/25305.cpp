/*
커트라인 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%BB%A4%ED%8A%B8%EB%9D%BC%EC%9D%B8-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main()
{
	int n,k;
	cin>>n>>k;
	vector<int> v(n);
	for(int i=0;i<n;i++)
	{
		cin>>v[i];
	}
	sort(v.begin(), v.end());
	cout<<v[n-k];
}
