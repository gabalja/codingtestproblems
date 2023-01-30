/*
서로 다른 부분 문자열의 개수 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%84%9C%EB%A1%9C-%EB%8B%A4%EB%A5%B8-%EB%B6%80%EB%B6%84-%EB%AC%B8%EC%9E%90%EC%97%B4%EC%9D%98-%EA%B0%9C%EC%88%98-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
	string s;
	cin>>s;
  vector<string> v(s.size());
	for(int i=0;i<s.size();i++)
	{
		for(int j=s.size()-i;j>0;j--)
		{
			v.push_back(s.substr(i,j));
		}
	}
	sort(v.begin(), v.end());
	v.erase(unique(v.begin(),v.end()),v.end());
	cout<<v.size()-1;
}
