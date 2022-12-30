/*
단어 공부 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%8B%A8%EC%96%B4-%EA%B3%B5%EB%B6%80-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
int main()
{
	string s;
	cin>>s;
	int max=-1;
	int cnt=0;
	int alpha[26]={0,};
	int c;
	transform(s.begin(),s.end(),s.begin(),(int(*)(int))toupper); // 대문자로 변환
	for(int i=0;i<s.length();i++)
	{
		alpha[s[i]-'A']++; // 알파벳 개수
	}
	for(int i=0;i<26;i++)
	{
		if(max<alpha[i]) // 가장 많이 나온 알파벳 찾기
		{
			max=alpha[i];
			c=i;
			cnt=0;
		}
		if(max==alpha[i]) cnt++; // 똑같은 개수의 알파벳이 여러개라면
	}
	if(cnt>1) cout<<"?";
	else cout<< (char)(c+'A');
}
