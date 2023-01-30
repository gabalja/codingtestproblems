/*
검문 C++ 풀이
https://doctcoder.tistory.com/entry/%EA%B2%80%EB%AC%B8-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>

using namespace std;

int main()
{
	int n;
	cin>>n;
	vector<int>v(n);
	for(int i=0;i<n;i++) cin>>v[i];
	sort(v.begin(),v.end());
	vector<int>v1;
	for(int i=1;i<n;i++) v1.push_back(v[i]-v[i-1]);
	int tmp=v1[0];
	for(int i=1;i<n-1;i++) tmp=gcd(tmp,v1[i]);
	vector<int>res;
	for(int i=2;i<pow(tmp,0.5)+1;i++)
	{
		if(tmp%i==0)
		{
			res.push_back(i);
			res.push_back(tmp/i);
		}
	}
	res.push_back(tmp);
	sort(res.begin(),res.end());
	res.erase(unique(res.begin(),res.end()),res.end());
	for(auto i:res) cout<<i<<' ';
}
