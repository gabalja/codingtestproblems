/*
킹, 퀸, 룩, 비숍, 나이트, 폰 C++ 풀이
https://doctcoder.tistory.com/entry/%ED%82%B9-%ED%80%B8-%EB%A3%A9-%EB%B9%84%EC%88%8D-%EB%82%98%EC%9D%B4%ED%8A%B8-%ED%8F%B0-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main() {
	int chess[6]={1,1,2,2,2,8}; // 원래 있어야 하는 피스 수
	int pieces[6]; // 현재 가지고 있는 피스 수
	for(int i=0; i<6; i++)
	{
		cin >> pieces[i];  
  }
	for(int i=0; i<6; i++)
	{
		cout << chess[i]-pieces[i]<<" ";  
  }
}
