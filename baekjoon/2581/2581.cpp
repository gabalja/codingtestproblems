/*
소수 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%86%8C%EC%88%98-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <cmath>

using namespace std;
int main()
{
  int m,n;
  scanf("%d",&m);
  scanf("%d",&n);
  int nums[10001]={0,};
  for(int j=2;j<10001;j++) nums[j]=j;
  for(int k=2;k<10001;k++)  // 에라토스테네스의 체
  {
    if(nums[k]==0) continue;
    for(int l=2*k;l<10001;l+=k) nums[l]=0;
  }
  int sum=0;
  int small=0;
  for(int h=n;h>=m;h--) // 최소의 소수와 소수들의 합을 찾음
  {
    if(nums[h]!=0)
    {
      sum+=nums[h];
      small=nums[h];
    }
  }
  if(sum==0) printf("%d",-1);
  else
  {
    printf("%d\n",sum);
    printf("%d",small);
  }
}
