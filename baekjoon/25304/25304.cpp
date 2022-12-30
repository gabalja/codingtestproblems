/*
영수증 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%98%81%EC%88%98%EC%A6%9D
*/
#include <iostream>

using namespace std;
int main()
{
	int x,n,a,b;
	cin>>x;
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cin>>a>>b;
		x-=a*b; // 물건 가격을 뺀다
	}
	if(x==0) // 물건 가격이 다 빠졌을때가 0이면, 즉 물건가격이랑 영수증 금액이 같다면
	{
		cout<<"Yes";
	}
	else
	{
		cout<<"No";
	}
}
