/*
수 정렬하기 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%88%98-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <vector>

using namespace std;
int main()
{
  int cnt, n;
	cin>>cnt;
	vector<int> nums;
	for(int i=0;i<cnt;i++)
	{
		cin>>n;
		nums.push_back(n);
	}
	for(int i=0;i<cnt;i++)
	{
		for(int j=i+1;j<cnt;j++)
		{
			if(nums[i]>nums[j]) swap(nums[i],nums[j]);
		}
	}
	for(int i=0;i<cnt;i++) cout<<nums[i]<<"\n";
}
