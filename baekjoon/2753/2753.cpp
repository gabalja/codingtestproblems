/*
윤년 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%9C%A4%EB%85%84-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main() {
  int year;
  cin >> year;
	if(year%4==0)
	{
		if(year%400==0)
		{
			cout<<1;
		}
		else if(year%100!=0)
		{
			cout<<1;
		}
		else
		{
			cout<<0;
		}
	}
	else
	{
		cout<<0;
	}
}
