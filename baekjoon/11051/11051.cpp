/*
이항 계수 2 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%9D%B4%ED%95%AD-%EA%B3%84%EC%88%98-2-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;

int main()
{
	int dp[1001][1001];
	int n,k;
	cin>>n>>k;
	dp[0][0]=1;
	dp[1][0]=1;
	dp[1][1]=1;
	for(int i=2;i<=n;i++)
	{
		for(int j=0;j<=i;j++)
		{
			if(j==0) dp[i][0]=1;
			else if(j==i) dp[i][j]=1;
			else dp[i][j]=(dp[i-1][j-1]+dp[i-1][j])%10007;
		}
	}
	cout<<dp[n][k];
}
