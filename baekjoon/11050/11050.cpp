/*
이항 계수 1 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%9D%B4%ED%95%AD-%EA%B3%84%EC%88%98-1-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;

int fac(int a)
{
	if(a==1||a==0) return 1;
	else return a*fac(a-1);
}

int main()
{
	int a,b;
	cin>>a>>b;
	cout<<fac(a)/fac(b)/fac(a-b);
}
