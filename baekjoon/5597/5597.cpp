/*
과제 안 내신 분..?  C++ 풀이
https://doctcoder.tistory.com/entry/%EA%B3%BC%EC%A0%9C-%EC%95%88-%EB%82%B4%EC%8B%A0-%EB%B6%84-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
	int arr[30]={0,};
	int inp;
	for(int i=0;i<28;i++) // 냈으면 0이 아니게 함
	{
		cin>>inp;
		arr[inp-1]++;
	}
	for(int i=0;i<30;i++) // 안 낸 사람 찾기
	{
		if(arr[i]==0) cout<<i+1<<"\n";
	}
}
