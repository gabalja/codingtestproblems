/*
ACM 호텔 C++ 풀이
https://doctcoder.tistory.com/entry/ACM-%ED%98%B8%ED%85%94-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
  int cases;  // 케이스
  cin>>cases;
  for(int i=0;i<cases;i++)
  {
    int num[3]; // 호텔의 층 수, 각 층의 방 수, 몇 번째 손님
    for(int j=0;j<3;j++) cin >> num[j];
    int a=num[2]%num[0];  // 배치할 층
    int b=num[2]/num[0]+1;  // 배치할 방, 방이 1부터 시작하므로 1을 더해줌
    if(a==0)  // 손님의 방이 호텔 층 수의 배수라면
    {
      a=num[0];
      b-=1;
    }
    if(b>=10) cout<<a<<b<<"\n"; // 방이 10개가 넘어간다면
    else cout<<a<<"0"<<b<<"\n"; // 중간에 0을 넣어야 함 
  }
}
