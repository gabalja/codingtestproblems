/*
팩토리얼 C++ 풀이
https://doctcoder.tistory.com/entry/%ED%8C%A9%ED%86%A0%EB%A6%AC%EC%96%BC-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int sol(int a)
{
  if(a==1||a==0) return 1; // 0!의 값은 1
  return a*sol(a-1);
}

int main()
{
  int n;
  scanf("%d",&n);
  printf("%d",sol(n));
}
