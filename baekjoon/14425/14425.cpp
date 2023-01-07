/*
문자열 집합 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%A7%91%ED%95%A9-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <unordered_set>
using namespace std;
int main()
{
  int n,m,a;
	int cnt=0;
	cin>>n>>m;
	string s;
	unordered_set<string>us;
	for(int i=0;i<n;i++)
	{
		cin>>s;
		us.insert(s);
	}
	for(int i=0;i<m;i++)
	{
		cin>>s;
		if(us.find(s)!=us.end()) cnt++;
	}
	cout<<cnt;
}
