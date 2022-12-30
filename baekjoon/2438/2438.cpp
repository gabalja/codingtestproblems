/*
별 찍기 - 1 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%B3%84-%EC%B0%8D%EA%B8%B0-1-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		for(int j=0;j<i;j++)
		{
			cout<<"*";
		}
		cout<<"\n";
	}
}
