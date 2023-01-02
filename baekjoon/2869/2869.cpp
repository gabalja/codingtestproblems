/*
달팽이는 올라가고 싶다 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%8B%AC%ED%8C%BD%EC%9D%B4%EB%8A%94-%EC%98%AC%EB%9D%BC%EA%B0%80%EA%B3%A0-%EC%8B%B6%EB%8B%A4-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
  int input[3]; // 입력
  for(int i=0;i<3;i++) cin >> input[i];
  int day=(input[2]-input[0])/(input[0]-input[1]);  // 마지막 날 전까지 소요되는 날들
  if(((input[2]-input[0])%(input[0]-input[1]))) day+=1; // day가 정수가 아니라면 하루 더 써야 함 
  cout << day +1; // 마지막 날 더하기
}
