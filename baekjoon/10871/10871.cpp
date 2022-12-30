/*
X보다 작은 수 C++ 풀이
https://doctcoder.tistory.com/entry/X%EB%B3%B4%EB%8B%A4-%EC%9E%91%EC%9D%80-%EC%88%98-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
	int n,x,inp;
	int arr[10000]={0,};
	cin>>n>>x;
	for(int i=0;i<n;i++) // 배열에 입력값 넣고
	{
		cin>>arr[i];
	}
	for(int i=0;i<10000;i++)
	{
		if(arr[i]==0) break; // 값이 없는 곳까지 갔으면 빠져나오기
		if(arr[i]<x) cout<<arr[i]<<" "; 
	}
}
