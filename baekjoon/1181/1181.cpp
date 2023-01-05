/*
단어 정렬 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%8B%A8%EC%96%B4-%EC%A0%95%EB%A0%AC-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(string s1, string s2)
{
	if(s1.size()==s2.size()) return s1<s2;
	else return s1.size()<s2.size();
}

int main()
{
	int n;
	cin>>n;
	vector<string> v;
	for(int i=0;i<n;i++)
	{
		string s;
		cin>>s;
		if(find(v.begin(),v.end(),s)==v.end()) v.push_back(s);
	}
	sort(v.begin(),v.end(),cmp);
	for(int i=0;i<v.size();i++)
	{
		cout<<v[i]<<"\n";
	}
}
