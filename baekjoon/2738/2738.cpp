/*
행렬 덧셈 C++ 풀이
https://doctcoder.tistory.com/entry/%ED%96%89%EB%A0%AC-%EB%8D%A7%EC%85%88-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
  int n,m;
	cin>>n>>m;
	int arr[101][101]={0,};
	for(int k=0;k<2;k++)
	{
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
				int inp;
				cin>>inp;
				arr[i][j]+=inp;
			}
		}
	}
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			cout<<arr[i][j]<<" ";
		}
		cout<<"\n";
	}
}
