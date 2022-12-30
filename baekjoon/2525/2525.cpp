/*
오븐 시계 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%98%A4%EB%B8%90-%EC%8B%9C%EA%B3%84-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
  	int hour,minute, cook;
  	cin >> hour>>minute;
	cin >> cook; // 조리시간
	minute+=cook;
	while(minute>=60) // 60분이 넘어가면
	{
		minute-=60;
		hour++;
		if(hour>=24) // 24시간이 지나면
		{
			hour-=24;
		}
	}
	cout<<hour<<" "<<minute;
}
