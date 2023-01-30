/*
배수와 약수 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%B0%B0%EC%88%98%EC%99%80-%EC%95%BD%EC%88%98-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;

int main()
{
	int a,b;
	while(true)
	{
		cin>>a>>b;
		if(a==0&&b==0) break;
		if(b%a==0) cout<<"factor\n";
		else if(a%b==0) cout<<"multiple\n";
		else cout<<"neither\n";
	}
}
