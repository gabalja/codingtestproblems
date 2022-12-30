/*
평균 C++ 풀이
https://doctcoder.tistory.com/entry/%ED%8F%89%EA%B7%A0-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
	int n;
	cin>>n;
	double max=-1;
	double arr[1000]={0,};
	double res=0;
	for(int i=0;i<n;i++)
	{
		cin>>arr[i];
		if(arr[i]>max) max=arr[i]; // 최대값 구하기
	}
	for(int i=0;i<n;i++)
	{
		arr[i]=arr[i]/max*100; // 새 점수 구하기
		res+=arr[i];
	}
	cout<<res/n;
}
