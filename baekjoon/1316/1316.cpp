/*
그룹 단어 체커 C++ 풀이
https://doctcoder.tistory.com/entry/%EA%B7%B8%EB%A3%B9-%EB%8B%A8%EC%96%B4-%EC%B2%B4%EC%BB%A4-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
  int cnt;
	cin>>cnt;
	int res=0;
	for(int i=0;i<cnt;i++)
	{
		string inp;
		cin>>inp;
		bool alpha[26]={false};
		bool check=true;
		for(int j=0;j<inp.length();j++)
		{
			if(alpha[inp[j]-'a'])
			{
				check=false;
        break;
			}
			alpha[inp[j]-'a']=true;
			char k=inp[j];
			while(1)
			{
				if(k!=inp[++j])
				{
					j-=1;
					break;
				}
			}
		}
		if(check==true) res+=1;
	}
	cout<<res;
}
