/*
A+B C++ 풀이
https://doctcoder.tistory.com/entry/AB-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <numeric>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int a,b;
		cin>>a>>b;
		cout<<lcm(a,b)<<"\n";
	}
}
