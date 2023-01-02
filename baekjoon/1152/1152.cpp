/*
단어의 개수 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%8B%A8%EC%96%B4%EC%9D%98-%EA%B0%9C%EC%88%98-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <string>

using namespace std;
int main() 
{
  string inp;
  getline(cin,inp);
  int cnt = 1;
  if(inp.empty()) cout << "0";
	else
	{
		for(int i = 0; i < inp.length(); i++)
 		{
  		if(inp[i] == ' ') cnt++;
  	}
  	if(inp[0] == ' ') cnt--;
		if(inp[inp.length()-1] == ' ') cnt--;
  	cout << cnt;
	}
}
