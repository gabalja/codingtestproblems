/*
직각삼각형 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%A7%81%EA%B0%81%EC%82%BC%EA%B0%81%ED%98%95-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;

int main()
{
  int a,b,c;
	while(true)
	{
		cin>>a>>b>>c;
		if(a==0&&b==0&&c==0) break;
		if(a*a==b*b+c*c) cout<<"right\n";
		else if(b*b==a*a+c*c) cout<<"right\n";
		else if(c*c==b*b+a*a) cout<<"right\n";
		else cout<<"wrong\n";
	}
}
