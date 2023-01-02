/*
벌집 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%B2%8C%EC%A7%91-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
  int n;  
  cin >> n; 
  int result=0; 
  int round=0;  
  int maxroom=1;  
  while(1)
  {
    maxroom += 6*round;  
    if(maxroom>=n)  
    {
      result=round+1; 
      break;
    }
    round++;
  }
  cout << result;
}
