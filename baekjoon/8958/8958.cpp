/*
OX퀴즈 C++ 풀이
https://doctcoder.tistory.com/entry/OX%ED%80%B4%EC%A6%88-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <string>

using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int res=0; // 최종 점수
		int cul=0; // 연속 점수
		string s;
		cin>>s;
		for(char c:s)
		{
			if(c=='O') // O을 만나면
			{
				cul++;
				res+=cul;
			}
			else
			{
				cul=0;
			}
		}
		cout<<res<<"\n";
	}
}
