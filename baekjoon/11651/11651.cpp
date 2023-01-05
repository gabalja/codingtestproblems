/*
좌표 정렬하기 2 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%A2%8C%ED%91%9C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-2-%ED%92%80%EC%9D%B4
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
		int a,b;
		cin>>a>>b;
		v.push_back(b);
		v.push_back(a);
		vv.push_back(v);
	}
	sort(vv.begin(), vv.end());
	for(int i=0;i<n;i++)
	{
		cout<<vv[i][1]<<" "<<vv[i][0]<<"\n";
	}
}
