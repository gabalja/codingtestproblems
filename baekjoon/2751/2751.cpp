/*
수 정렬하기 2 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%88%98-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-2-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
  int num;
  cin >> num;
  vector<int>nums;
  int a;
  for(int i=0;i<num;i++)
  {
    cin >> a;
    nums.push_back(a);
  }
  sort(nums.begin(),nums.end());
  for(int i=0;i<num;i++) cout << nums[i] << "\n";
}
