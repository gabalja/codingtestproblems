/*
상수 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%83%81%EC%88%98-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main() 
{
  int a, b;
	cin >> a>> b;
	int na=(a%10)*100+((a/10)%10)*10+a/100;
	int nb=(b%10)*100+((b/10)%10)*10+b/100;
	if(na>nb) cout<<na;
	else cout<<nb;
}
