/*
링 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%A7%81-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main()
{
	int n;
	cin>>n;
	vector<int>v(n);
	for(int i=0;i<n;i++) cin>>v[i];
	for(int i=1;i<n;i++)
	{
		int g=gcd(v[0],v[i]);
		cout<<v[0]/g<<'/'<<v[i]/g<<"\n";
	}
}
