/*
크로아티아 알파벳 C++ 풀이
https://doctcoder.tistory.com/entry/%ED%81%AC%EB%A1%9C%EC%95%84%ED%8B%B0%EC%95%84-%EC%95%8C%ED%8C%8C%EB%B2%B3-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <string>

using namespace std;
int main()
{
  string croatian[8] = {"c=","c-","dz=","d-","lj","nj","s=","z="};
  int idx;
  string inp;
  cin >> inp;
  for(int i = 0; i < 8; i++)
  {
    while(1)
		{
      idx = inp.find(croatian[i]);
      if(idx == string::npos)
        break;
      inp.replace(idx,croatian[i].length(),"0");
    }
  }
  cout << inp.length();
}
