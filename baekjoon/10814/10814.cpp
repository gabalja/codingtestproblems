/*
나이순 정렬 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%82%98%EC%9D%B4%EC%88%9C-%EC%A0%95%EB%A0%AC-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool comp(pair<int,pair<int,string>> a,pair<int,pair<int,string>> b)
{
	if(a.second.first==b.second.first) return a.first<b.first;
	else return a.second.first<b.second.first;
}

int main()
{
	int n,age;
	string name;
	cin>>n;
	vector<pair<int,pair<int,string>>> user;
	for(int i=0;i<n;i++)
	{
		cin>>age>>name;
		user.push_back(pair<int,pair<int,string>>(i,pair<int,string>(age,name)));
	}
	sort(user.begin(),user.end(),comp);
	for(int i=0;i<n;i++)
	{
		cout<<user[i].second.first<<" "<<user[i].second.second<<"\n";
	}
}
