/*
다리 놓기 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%8B%A4%EB%A6%AC-%EB%86%93%EA%B8%B0-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int n,m;
		cin>>n>>m;
		int nn;
		if(n>=m-n) nn=n;
		else nn=m-n;
		long long res=1;
		for(int j=1;j<=m-nn;j++)
		{
			res=int(res*(m+1-j)/j);
		}
		cout<<res<<'\n';
	}
}
