/*
숫자의 합 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%88%AB%EC%9E%90%EC%9D%98-%ED%95%A9-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
	int n;
	cin>>n;
	int arr[n];
	int sum=0;
	for(int i=0;i<n;i++)
	{
    		scanf("%1d",&arr[i]);
	}
	for(int a:arr)
	{
		sum+=a;
	}
	cout<<sum;
}
