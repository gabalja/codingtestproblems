/*
별 찍기 - 2 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%B3%84-%EC%B0%8D%EA%B8%B0-2-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		for(int k=n-i;k>0;k--) // 공백 먼저 적용
		{
			cout<<" ";
		}
		for(int j=0;j<i;j++) // 별 찍기
		{
			cout<<"*";
		}
		cout<<"\n";
	}
}
