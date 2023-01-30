/*
터렛 C++ 풀이
https://doctcoder.tistory.com/entry/%ED%84%B0%EB%A0%9B-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
  int t;
	cin>>t;
  while(t!=0)
  {
    int count=0;
    int x1,y1,r1,x2,y2,r2;
    cin>>x1>>y1>>r1>>x2>>y2>>r2;
    double dis=sqrt(pow(x1-x2,2)+pow((y1-y2),2));
    int rsum=r1+r2;	
    int rsub=(r1>r2)?r1-r2:r2-r1;	
    if(dis!=0)	// 
    {
      if(rsum==dis) count++;
      else if (rsub==dis) count++;
      else if (rsum<dis) count+=0;
      else if (dis<rsub) count+=0;
      else count+=2;
    }
    else
    {
      if(r1==r2)
      {
				cout<<"-1\n";
        t--;
        continue;
      }
    }
		cout<<count<<"\n";
    t--;
  }
}
