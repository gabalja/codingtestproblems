/*
합 C++ 풀이
https://doctcoder.tistory.com/entry/%ED%95%A9-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
	int n;
	cin>>n;
	int result=0;
	for(int i=1;i<=n;i++)
	{
		result+=i;
	}
	cout<<result;
}
