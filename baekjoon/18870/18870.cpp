/*
좌표 압축 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%A2%8C%ED%91%9C-%EC%95%95%EC%B6%95-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int n;
	cin>>n;
	vector<long long> v1; // 모든 입력
	vector<long long> v2; // 중복 아닌 것만
	for(int i=0;i<n;i++)
	{
		long long inp;
		cin>>inp;
		v1.push_back(inp);
		v2.push_back(inp);
	}
	sort(v2.begin(),v2.end());
	v2.erase(unique(v2.begin(),v2.end()),v2.end()); 
	for(int i=0;i<n;i++)
	{
		cout<<lower_bound(v2.begin(),v2.end(),v1[i])-v2.begin()<<" ";
	}
}
