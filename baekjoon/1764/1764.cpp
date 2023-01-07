/*
듣보잡 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%93%A3%EB%B3%B4%EC%9E%A1-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
int main()
{
  int n,m,cnt=0;
	string s;
	cin>>n>>m;
	map<string,bool>nv;
	vector<string>res;
	for(int i=0;i<n;i++)
	{
		cin>>s;
		nv.insert(make_pair(s,true));
	}
	for(int i=0;i<m;i++)
	{
		cin>>s;
		if(nv[s])
		{
			cnt++;
			res.push_back(s);
		}
	}
	sort(res.begin(),res.end());
	cout<<cnt<<"\n";
	for(int i=0;i<res.size();i++)
	{
		cout<<res[i]<<"\n";
	}
}
