/*
소트인사이드 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%86%8C%ED%8A%B8%EC%9D%B8%EC%82%AC%EC%9D%B4%EB%93%9C-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <algorithm>

using namespace std;
int main()
{
	string s;
	cin>>s;
	sort(s.begin(),s.end(),greater<char>());
	cout<<s;
}
