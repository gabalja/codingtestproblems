/*
최댓값 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%B5%9C%EB%8C%93%EA%B0%92-%ED%92%80%EC%9D%B4-1
*/
#include <iostream>

using namespace std;
int main()
{
	int arr[9][9]={0,};
	int max=-1;
	int x,y;
	for(int i=0;i<9;i++)
	{
		for(int j=0;j<9;j++)
		{
			cin>>arr[i][j];
			if(arr[i][j]>max)
			{
				max=arr[i][j];
				x=i;
				y=j;
			}
		}
	}
	cout<<max<<"\n";
	cout<<x+1<<" "<<y+1;
}
