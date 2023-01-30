/*
네 번째 점 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%84%A4-%EB%B2%88%EC%A7%B8-%EC%A0%90-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;

int main()
{
  int x[3]; 
  int y[3]; 
  int rex,rey;
  for(int i=0;i<3;i++) cin>>x[i]>>y[i];
  if(x[0]==x[1]) rex=x[2];
  else if (x[0]==x[2]) rex=x[1];
  else rex=x[0];
  if(y[0]==y[1]) rey=y[2];
  else if (y[0]==y[2]) rey=y[1];
  else rey=y[0];
  cout<<rex<<" "<<rey;
}
