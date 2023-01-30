/*
직사각형에서 탈출 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95%EC%97%90%EC%84%9C-%ED%83%88%EC%B6%9C-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;

int main()
{
  int x,y,w,h;
	cin>>x>>y>>w>>h;
  int l1,l2;
  l1=w-x; 
  l2=h-y;  
  int dis1=(l1>x)?x:l1; 
  int dis2=(l2>y)?y:l2; 
  int dis3=(dis1>dis2)?dis2:dis1; 
	cout<<dis3;
}
