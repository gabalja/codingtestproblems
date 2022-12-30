/*
평균은 넘겠지 C++ 풀이
https://doctcoder.tistory.com/entry/%ED%8F%89%EA%B7%A0%EC%9D%80-%EB%84%98%EA%B2%A0%EC%A7%80-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main()
{
	int c,num;
	cin>>c;
	int arr[1000]={0,};
	double mean;
	for(int i=0;i<c;i++)
	{
		cin>>num; // 학생 수
		int sum=0;
		for(int j=0;j<num;j++)
		{
			cin>>arr[j];
			sum+=arr[j];
		}
		mean=(double)sum/(double)num; // 평균
		int count=0;
		for(int j=0;j<num;j++)
		{
			if(arr[j]>mean) count++;
		}
		double res= (double)count/(double)num*100; // 비율
		cout<<fixed; // 소수점 셋째 자리 반올림
		cout.precision(3);
		cout<<res<<"%"<<"\n";
	}
}
