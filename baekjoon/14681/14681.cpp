/*
사분면 고르기 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%82%AC%EB%B6%84%EB%A9%B4-%EA%B3%A0%EB%A5%B4%EA%B8%B0-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main() {
  int x,y;
  cin >> x;
	cin >> y;
	if(x>0&&y>0)
	{
		cout<<1;
	}
	if(x<0&&y>0)
	{
		cout<<2;
	}
	if(x<0&&y<0)
	{
		cout<<3;
	}
	if(x>0&&y<0)
	{
		cout<<4;
	}
}
