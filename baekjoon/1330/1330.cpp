/*
두 수 비교하기 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%91%90-%EC%88%98-%EB%B9%84%EA%B5%90%ED%95%98%EA%B8%B0-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main() {
	int A, B;
	cin>>A>>B;
	if(A>B)
	{
		cout<<">";
	}
	else if(A<B)
	{
		cout<<"<";
	}
	else if(A==B)
	{
		cout<<"==";
	}
}
