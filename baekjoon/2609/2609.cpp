/*
최대공약수와 최소공배수 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%99%80-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <numeric>

using namespace std;

int main()
{
	int a,b;
	cin>>a>>b;
	cout<<gcd(a,b)<<"\n";
	cout<<lcm(a,b);
}
