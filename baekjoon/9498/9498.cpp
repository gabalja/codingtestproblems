/*
시험 성적 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%8B%9C%ED%97%98-%EC%84%B1%EC%A0%81-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main() {
	int score;
	cin>>score;
	if(score>89)
	{
		cout<<"A";
	}
	else if(score>79)
	{
		cout<<"B";
	}
	else if(score>69)
	{
		cout<<"C";
	}
	else if(score>59)
	{
		cout<<"D";
	}
	else{
		cout<<"F";
	}
}
