/*
설탕 배달 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%84%A4%ED%83%95-%EB%B0%B0%EB%8B%AC-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int solve(int n)
{
  int threes=0; // 3kg 봉지
  int fives=n/5;  // 5kg 봉지
  n%=5;
  while(fives>=0) 
  {
    if(n%3==0)  // 3kg으로 나눠질 수 있다면
    {
      threes=n/3;
      n%=3;
      break;
    }
    fives-=1;
    n+=5;
  }
  if(n==0) return fives+threes; // 3kg와 5kg로 잘 나누어졌다면
  else return -1; // 나눌 수 없다면
}

int main()
{
  int t;
  scanf("%d",&t);
  printf("%d",solve(t));
}
