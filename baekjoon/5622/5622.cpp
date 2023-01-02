/*
다이얼 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%8B%A4%EC%9D%B4%EC%96%BC-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main() 
{
	int alpha[]={3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10};
  string inp;
	cin>>inp;
	int time=0;
	for(int i=0;i<inp.length();i++)
	{
		time+=alpha[inp[i]-65];
	}
	cout<<time;
}
