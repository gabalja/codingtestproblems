/*
별 찍기 - 10 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%B3%84-%EC%B0%8D%EA%B8%B0-10-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
void sol(int a,int b, int c)
{
  if((a/c)%3==1&&(b/c)%3==1) printf(" ");
  else
  {
    if(c/3==0) printf("*");
    else sol(a,b,c/3);
  }
}

int main()
{
  int n;
  scanf("%d",&n);
  for(int i=0;i<n;i++)
  {
    for(int j=0;j<n;j++) sol(i,j,n);
    printf("\n");
  }
}
