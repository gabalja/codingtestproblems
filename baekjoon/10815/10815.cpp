/*
숫자 카드 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%88%AB%EC%9E%90-%EC%B9%B4%EB%93%9C-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
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
	for(int i=0;i<m;i++)
	{
		cin>>a;
		mv.push_back(a);
	}
	sort(nv.begin(),nv.end());
	for(int i=0;i<m;i++)
	{
		if (binary_search(nv.begin(),nv.end(),mv[i])) cout<<1<<" ";
		else cout<<0<<" ";
	}
}
