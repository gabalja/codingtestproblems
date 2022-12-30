/*
문자열 반복 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%B0%98%EB%B3%B5-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <string>

using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int r;
		string s;
		cin>>r;
		cin>>s;
		for(char c:s) // s에 있는 모든 문자에 대해
		{
			for(int j=0;j<r;j++) cout<<c; // r만큼 반복
		}
		cout<<"\n";
	}
}
