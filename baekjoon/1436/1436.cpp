/*
영화감독 숌 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%98%81%ED%99%94%EA%B0%90%EB%8F%85-%EC%88%8C-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
  int n;
  scanf("%d",&n);
  int count=0;
  int num;
  for(num=666;count<n;num++)
  {
    for(int i=num;i>0;i/=10)
    {
      if(i%1000==666)
      {
        count++;
        break;
      }
    }
  }
  printf("%d",num-1);
}
