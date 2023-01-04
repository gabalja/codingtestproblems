/*
좌표 정렬하기 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%A2%8C%ED%91%9C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include<vector>
#include<algorithm>

using namespace std;
int main()
{
	int n;
	cin>>n;
	vector<vector<int>> vv;
	for(int i=0;i<n;i++)
	{
		vector<int> v;
		int inp;
		for(int j=0;j<2;j++)
		{
			cin>>inp;
			v.push_back(inp);
		}
		vv.push_back(v);
	}
	sort(vv.begin(), vv.end());
	for(int i=0;i<n;i++)
	{
		cout<<vv[i][0]<<" "<<vv[i][1]<<"\n";
	}
}
