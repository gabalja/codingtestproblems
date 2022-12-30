/*
최소, 최대 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%B5%9C%EC%86%8C-%EC%B5%9C%EB%8C%80-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
	int n,maxnum,minnum,a;
	cin>>n;
	maxnum=-2000000;
	minnum=2000000;
	for(int i=0;i<n;i++)
	{
		cin>>a;
		if(a>maxnum) maxnum=a;
		if(a<minnum) minnum=a;
	}
	cout<<minnum<<" "<<maxnum;
}
