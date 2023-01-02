/*
분수찾기 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%B6%84%EC%88%98%EC%B0%BE%EA%B8%B0-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
  int x;  // 입력
  cin>>x;
  int count=0;  // 지그재그의 순서
  while(x>0)  // x = 떨어져 있는 거리
  {
    count++;
    x-=count;
  }
  if(count%2==0) cout << count+x << "/" << 1-x; // 짝수면 분자가 증가
  else cout << 1-x << "/" << count +x; // 홀수면 분모가 증가
}
