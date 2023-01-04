/*
소인수분해 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%86%8C%EC%9D%B8%EC%88%98%EB%B6%84%ED%95%B4-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
  int n;
  scanf("%d",&n);
  int div=2;  // 인수
  if(n!=1)
  {
    while(n>1)
    {
      if(n%div==0)  // 나눠지면 인수 출력
      {
        printf("%d\n",div);
        n/=div;
      }
      else div++; // 안나눠지면 인수 증가
    }
  }
}
