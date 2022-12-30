/*
주사위 세개 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%A3%BC%EC%82%AC%EC%9C%84-%EC%84%B8%EA%B0%9C-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
	int one, two, three;
	cin >>one>>two>>three;
	if(one==two&&two==three) // 셋 다 같으면
	{
		cout<<one*1000+10000;
	}
	else if(one==two||one==three) // 두개만 같다면
	{
		cout<<one*100+1000;
	}
	else if(two==three)
	{
		cout<<two*100+1000;
	}
	else
	{
		cout<<max(max(one,two),three)*100;
	}
}
