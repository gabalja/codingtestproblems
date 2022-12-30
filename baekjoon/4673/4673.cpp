/*
셀프 넘버 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%85%80%ED%94%84-%EB%84%98%EB%B2%84-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;

int selfnum(int n) // 셀프 넘버가 아닌 수를 생성
{
	int sum=n;
	while(n!=0)
	{
		sum+=n%10;
		n/=10;
	}
	return sum;
}

int main()
{
	int arr[10001]={0,};
	for(int i=1;i<10001;i++)
	{
		int idx=selfnum(i);
		if(idx<=10001) // 10000까지만 구하면 됌
		{
			arr[idx]=1;
		}
	}
	for(int i=1;i<10001;i++)
	{
		if(arr[i]!=1) // 남은건 셀프 넘버 뿐
		{
			cout<<i<<"\n";
		}
	}
}
