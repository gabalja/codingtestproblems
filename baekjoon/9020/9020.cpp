/*
골드바흐의 추측 C++ 풀이
https://doctcoder.tistory.com/entry/%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90%EC%9D%98-%EC%B6%94%EC%B8%A1-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
const int range=10001;
int main()
{
  int nums[range]={0,};
  for(int j=2;j<range;j++) nums[j]=j;
  for(int k=2;k<range;k++)  // 에라토스테네스의 체
  {
    if(nums[k]==0) continue;
    for(int l=2*k;l<range;l+=k) nums[l]=0;
  }
  int t;
  scanf("%d",&t);
  while(t!=0)
  {
    int n;
    scanf("%d",&n);
    int g1=0;
    int g2=0;  //  골드바흐 파티션
    for(int h=n/2;h<n;h++)
    {
      if(nums[h]!=0 && nums[n-h]!=0)  // 파티션끼리 차이가 적게 하기 위함
      {
        g2=nums[h];
        g1=n-g2;
        break;
      }
    }
    printf("%d %d\n",g1,g2);
    t--;
  }
}
