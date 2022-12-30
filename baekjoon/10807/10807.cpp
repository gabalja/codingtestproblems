/*
개수 세기 C++ 풀이
https://doctcoder.tistory.com/entry/%EA%B0%9C%EC%88%98-%EC%84%B8%EA%B8%B0-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
	int n,v,count;
	count=0;
	int arr[100]={0,}; // 0으로 배열 초기화
	cin>>n;
	for(int i=0;i<n;i++) // 배열에 입력값 넣기
	{
		cin>>arr[i];
	}
	cin>>v;
	for(int i=0;i<n;i++)
	{
		if(arr[i]==v) count++;
	}
	cout<<count;
}
