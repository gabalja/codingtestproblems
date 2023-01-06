/*
덩치 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%8D%A9%EC%B9%98-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <vector>
using namespace std;
int main()
{
  int n,a,b;
  cin>>n;
	vector<int> weight;
	vector<int> height;
	vector<int> ranks(n);
	fill(ranks.begin(),ranks.end(),1);
	for(int i=0;i<n;i++)
	{
		cin>>a>>b;
		weight.push_back(a);
		height.push_back(b);
	}
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			if(weight[i]>weight[j]&&height[i]>height[j]) ranks[j]++;
		}
	}
	for(int i=0;i<n;i++)
	{
		cout<<ranks[i]<<" ";
	}
}
