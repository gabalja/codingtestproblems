/*
소수 구하기 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%86%8C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
const int range=1000001;
int main()
{
  int m,n;
  scanf("%d %d",&m,&n);
  int nums[range]={0,};
  for(int j=2;j<range;j++) nums[j]=j;
  for(int k=2;k<range;k++)  // 에라토스테네스의 체
  {
    if(nums[k]==0) continue;
    for(int l=2*k;l<range;l+=k) nums[l]=0;
  }
  for(int h=m;h<=n;h++) // 출력
  {
    if(nums[h]!=0) printf("%d\n",nums[h]);
  }
}
