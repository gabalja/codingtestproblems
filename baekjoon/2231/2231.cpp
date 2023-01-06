/*
분해합 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%B6%84%ED%95%B4%ED%95%A9-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <vector>
using namespace std;
int main()
{
  int n;
  cin>>n;
	for(int i=1;i<n+1;i++)
	{
		int ii=i;
		int check=ii;
		while(ii>0)
		{
			check+=ii%10;
			ii/=10;
		}
		if(check==n)
		{
			cout<<i;
			break;
		}
		if(i==n) cout<<0;
	}
}
