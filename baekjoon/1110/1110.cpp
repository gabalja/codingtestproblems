/*
더하기 사이클 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%8D%94%ED%95%98%EA%B8%B0-%EC%82%AC%EC%9D%B4%ED%81%B4-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
	int n,cycle,nn;
	cin>>n;
	nn=n;
	cycle=0;
	do
	{
		nn=(nn%10)*10+((nn/10)+(nn%10))%10;
		cycle++;
	}
	while(nn!=n);
	cout<<cycle;
}
