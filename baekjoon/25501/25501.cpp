/*
재귀의 귀재 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%9E%AC%EA%B7%80%EC%9D%98-%EA%B7%80%EC%9E%AC-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <string>
#include <string.h>

using namespace std;

int cnt=0;

int recursion(const string& s, int l, int r)
{
	cnt++;
	if (l >= r) return 1;
	else if (s[l] != s[r]) return 0;
	else return recursion(s, l + 1, r - 1);
}

int isPalindrome(const string& s)
{
	return recursion(s,0,s.length() - 1);
}

int main()
{
	int t;
	cin>>t;
	string ss;
	for(int i=0;i<t;i++)
	{
		cin>>ss;
		cout<<isPalindrome(ss)<<" "<<cnt<<"\n";
		cnt=0;
	}
}
