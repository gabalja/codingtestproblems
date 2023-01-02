/*
손익분기점 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%86%90%EC%9D%B5%EB%B6%84%EA%B8%B0%EC%A0%90-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
  int nums[3];	
  for(int i=0;i<3;i++) cin >> nums[i];	
  if(nums[1]>=nums[2]) cout << -1;
  else cout << (nums[0]/(nums[2]-nums[1]))+1; 
}
