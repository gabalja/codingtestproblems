/*
나머지 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%82%98%EB%A8%B8%EC%A7%80-%ED%92%80%EC%9D%B4-1
*/
#include <iostream>

using namespace std;
int main()
{
	int arr[42]={0,}; // 42의 나머지는 0부터 41임
	int inp;
	int count=0;
	for(int i=0;i<10;i++)
	{
		cin>>inp;
		arr[inp%42]++; // 나머지가 담긴 배열의 칸을 0이 아닌 값으로 변경
	}
	for(int i=0;i<42;i++) // 0이 아닌 칸의 수를 센다
	{
		if(arr[i]!=0) count++;
	}
	cout<<count;
}
