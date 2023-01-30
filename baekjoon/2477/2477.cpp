/*
참외밭 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%B0%B8%EC%99%B8%EB%B0%AD-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;

int main()
{
	pair<int,int> cor[12];
	int k,a,b,ba,sa;
	cin>>k;
	for(int i=0;i<6;i++)
	{
		cin>>a>>b;
		cor[i]=cor[i+6]={a,b};
	}
	for(int i=0;i<12;i++)
	{
		if(cor[i].first==cor[i-2].first&&cor[i-1].first==cor[i-3].first)
		{
			ba=cor[i+1].second*cor[i+2].second;
			sa=cor[i-1].second*cor[i-2].second;
			break;
		}
	}
	cout<<k*(ba-sa);
}
