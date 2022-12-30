/*
빠른 A+B C++ 풀이
https://doctcoder.tistory.com/entry/%EB%B9%A0%EB%A5%B8-AB-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int t,a,b;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		cin>>a>>b;
		cout<<a+b<<"\n";
	}
}
