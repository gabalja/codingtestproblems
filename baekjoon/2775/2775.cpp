/*
부녀회장이 될테야 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%B6%80%EB%85%80%ED%9A%8C%EC%9E%A5%EC%9D%B4-%EB%90%A0%ED%85%8C%EC%95%BC-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int aprt[15][15]={0}; 
int main()
{
  for(int j=0;j<15;j++) // 0층에 있는 사람 구함
  {
    aprt[0][j]=j+1;
  }
  for(int a=1;a<15;a++) // 1층부터 14층까지
  {
    for(int b=0;b<15;b++) // 0호부터 14호까지
    {
      for(int c=0;c<=b;c++) // 어느 호에 몇 명이 사는지 계산
      {
        aprt[a][b]+=aprt[a-1][c];
      }
    }
  }
  int t;
  cin>>t;
  for(int i=0;i<t;i++)
  {
    int k,n;
    cin >> k;
    cin >> n;  
    cout << aprt[k][n-1]<<"\n"; // 출력
  }
}
