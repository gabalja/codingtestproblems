/*
하노이 탑 이동 순서 C++ 풀이
https://doctcoder.tistory.com/entry/%ED%95%98%EB%85%B8%EC%9D%B4-%ED%83%91-%EC%9D%B4%EB%8F%99-%EC%88%9C%EC%84%9C-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include<cmath>

using namespace std;

void hanoi(int k,int a, int b, int c)
{
  if(k==1) printf("%d %d\n",a,b);
  else
  {
    hanoi(k-1,a,c,b);
    printf("%d %d\n",a,b);
    hanoi(k-1,c,b,a);
  }
}

int main()
{
  int n;
  scanf("%d",&n);
  cout << (int)pow(2,n)-1 << "\n";
  hanoi(n,1,3,2);
}
