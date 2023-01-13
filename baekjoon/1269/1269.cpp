/*
대칭 차집합 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%8C%80%EC%B9%AD-%EC%B0%A8%EC%A7%91%ED%95%A9-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <set>
#include <vector>
#include <algorithm> 

using namespace std;
int main()
{
  int n,m;
	cin>>n>>m;
	set<int> a;
	set<int> b;
	vector<int> res;
	for(int i=0;i<n;i++)
	{
		int nn;
		cin>>nn;
		a.insert(nn);
	}
	for(int i=0;i<m;i++)
	{
		int nn;
		cin>>nn;
		b.insert(nn);
	}
	set_symmetric_difference(a.begin(),a.end(),b.begin(),b.end(),back_inserter(res));
	cout<<res.size();
}
