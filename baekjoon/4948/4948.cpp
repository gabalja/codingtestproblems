/*
베르트랑 공준 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%B2%A0%EB%A5%B4%ED%8A%B8%EB%9E%91-%EA%B3%B5%EC%A4%80-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
const int range=123457; // 문제 범위
int main()
{
  int nums[2*range]={0,};
  for(int j=2;j<2*range;j++) nums[j]=j;
  for(int k=2;k<2*range;k++)  // 에라토스테네스의 체
  {
    if(nums[k]==0) continue;
    for(int l=2*k;l<2*range;l+=k) nums[l]=0;
  }
  while(1)
  {
    int n;
    scanf("%d",&n);
    if(n==0) break;
    int count =0;
    for(int h=n+1;h<=2*n;h++)
    {
      if(nums[h]!=0) count+=1;
    }
    printf("%d\n",count);
  }
}
