/*
블랙잭 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%B8%94%EB%9E%99%EC%9E%AD-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <vector>
using namespace std;
int main()
{
  int n,m,inp;
  cin>>n>>m;
	int mcheck=0;
	vector<int> v;
	for(int i=0;i<n;i++)
	{
		cin>>inp;
		v.push_back(inp);
	}
	for(int i=0;i<n-2;i++)
	{
		for(int j=i+1;j<n-1;j++)
		{
			for(int k=j+1;k<n;k++)
			{
				int nmcheck=v[i]+v[j]+v[k];
				if(nmcheck<=m&&mcheck<nmcheck)
				{
					mcheck=nmcheck;
				}
			}
		}
	}
	cout<<mcheck;
}
