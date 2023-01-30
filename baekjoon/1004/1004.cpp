/*
어린 왕자 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%96%B4%EB%A6%B0-%EC%99%95%EC%9E%90-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
  int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int cnt=0;
		int x1,y1,x2,y2,n;
		cin>>x1>>y1>>x2>>y2;
		cin>>n;
		vector<int> cx(n);
		vector<int> cy(n);
		vector<int> cr(n);
		for(int j=0;j<n;j++) cin>>cx[j]>>cy[j]>>cr[j];
		for(int j=0;j<n;j++)
		{
			double sdis=pow(pow(x1-cx[j],2)+pow(y1-cy[j],2),0.5);
			double edis=pow(pow(x2-cx[j],2)+pow(y2-cy[j],2),0.5);
			double r=cr[j];
			if(sdis<r)
			{
				if(r<edis) cnt++;
			}
			else if(r>edis) cnt++;
		}
		cout<<cnt<<"\n";
	}
}
