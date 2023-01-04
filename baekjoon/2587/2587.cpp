/*
대표값2 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%8C%80%ED%91%9C%EA%B0%922-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
int main()
{
	vector<int> v;
	int mean=0;
	for(int i=0;i<5;i++)
	{
		int inp;
		cin>>inp;
		v.push_back(inp);
		mean+=inp;
	}
	sort(v.begin(), v.end());
	cout<<mean/5<<"\n";
	cout<<v[2];
}
