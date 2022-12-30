/*
최댓값 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%B5%9C%EB%8C%93%EA%B0%92-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
	int arr[9]={0,}; // 배열 선언
	int idx; // 위치
	int maxnum=-1;
	for(int i=0;i<9;i++)
	{
		cin>>arr[i];
		if(arr[i]>maxnum)
		{
			maxnum=arr[i];
			idx=i+1;
		}
	}
	cout<<maxnum<<"\n";
	cout<<idx;
}
