/*
알람 시계 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%95%8C%EB%9E%8C-%EC%8B%9C%EA%B3%84-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
  int hour,minute;
  cin >> hour>>minute;
  if(minute<45) // 45분을 바로 빼지 못한다면
  {
  	hour--;
	minute+=60;
  }
  if(hour<0) // 시간이 음수가 된다면
  {
  	hour+=24;
  }
  cout<<hour<<" "<<minute-45;
}
