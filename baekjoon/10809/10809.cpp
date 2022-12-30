/*
알파벳 찾기 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%95%8C%ED%8C%8C%EB%B2%B3-%EC%B0%BE%EA%B8%B0-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <string>

using namespace std;
int main()
{
	string alpha="abcdefghijklmnopqrstuvwxyz";
	string s;
	cin>>s;
	for(int i=0;i<alpha.length();i++)
	{
		cout<<(int)s.find(alpha[i])<<" "; // find 사용, -1을 출력하기 위해 int형으로 변환
	}
}
