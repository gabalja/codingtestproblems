/*
택시 기하학 C++ 풀이
https://doctcoder.tistory.com/entry/%ED%83%9D%EC%8B%9C-%EA%B8%B0%ED%95%98%ED%95%99-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
const double pi = 3.1415926535897;
int main()
{
	cout << fixed;
	cout.precision(6);
	int r;
	double eure,tare;
	cin>>r;
	eure=pi*r*r;
	tare=double(r*r*2);
	cout<<eure<<"\n";
	cout<<tare<<"\n";
}
