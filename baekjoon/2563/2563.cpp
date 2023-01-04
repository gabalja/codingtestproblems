/*
색종이 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%83%89%EC%A2%85%EC%9D%B4-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
	int arr[101][101]={0,};
	int n,x,y;
	int area=0;
	cin>>n;
	for(int k=0;k<n;k++)
	{
		cin>>x>>y;
		for(int i=x;i<x+10;i++)
		{
			for(int j=y;j<y+10;j++)
			{
				arr[i][j]=1;
			}
		}
	}
	for(int i=0;i<101;i++)
	{
		for(int j=0;j<101;j++)
		{
			if(arr[i][j]==1) area+=1;
		}
	}
	cout<<area;
}
