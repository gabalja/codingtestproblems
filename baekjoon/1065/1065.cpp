/*
한수 C++ 풀이
https://doctcoder.tistory.com/entry/%ED%95%9C%EC%88%98-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;

int han(int n)
{
	int ret;
	if(n<100) // 두자리수는 모두 한수
	{
		ret=1;
	}
	else if(((n/100)-((n/10)%10))==(((n/10)%10)-(n%10))) // 세자리수 중 한수 판별
	{
		ret=1;
	}
	else
	{
		ret=0;
	}
	return ret;
}

int main()
{
	int arr[1001]={0,};
	int n;
	cin>>n;
	int count=0;
	for(int i=1;i<=n;i++)
	{
		arr[i]=han(i); // 1이면 한수, 0이면 한수 아님
		if(arr[i]!=0) count++; // 한수 개수 세기
	}
	cout<<count;
}
