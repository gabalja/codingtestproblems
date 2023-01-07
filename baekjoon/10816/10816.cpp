/*
숫자 카드 2 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%88%AB%EC%9E%90-%EC%B9%B4%EB%93%9C-2-%ED%92%80%EC%9D%B4
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
  int n,m,a;
	cin>>n;
	vector<int>nv;
	vector<int>mv;
	for(int i=0;i<n;i++)
	{
		cin>>a;
		nv.push_back(a);
	}
	cin>>m;
	sort(nv.begin(),nv.end());
	for(int i=0;i<m;i++)
	{
		cin>>a;
		auto up=upper_bound(nv.begin(),nv.end(),a);
		auto dn=lower_bound(nv.begin(),nv.end(),a);
		mv.push_back(up-dn);
	}
	for(auto b:mv)
	{
		cout<<b<<" ";
	}
}
