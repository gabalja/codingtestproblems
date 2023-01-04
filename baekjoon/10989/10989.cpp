/*
수 정렬하기 3 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%88%98-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-3-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
	ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
	int n;
	cin>>n;
	int arr[10001] = {0};
	for(int i=0;i<n;i++)
	{
		int inp;
		cin>>inp;
		arr[inp]+=1;
	}
	for(int i=1;i<10001;i++)
	{
		for(int j=0;j<arr[i];j++)
		{
			cout<<i<<"\n";
		}     
	}
}
