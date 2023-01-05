/*
피보나치 수 5 C++ 풀이
https://doctcoder.tistory.com/entry/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98-5-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int sol(int a)
{
  if(a==0) return 0;
  if(a==1) return 1;
  return sol(a-1)+sol(a-2);
}

int main()
{
  int n;
  scanf("%d",&n);
  printf("%d",sol(n));
}
