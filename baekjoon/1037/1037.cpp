/*
약수 C++ 풀이
https://doctcoder.tistory.com/entry/%EC%95%BD%EC%88%98-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int n;
	cin>>n;
	vector<int> v(n);
	for(int i=0;i<n;i++) cin>>v[i];
	sort(v.begin(),v.end());
	cout<<v[0]*v[n-1];
}
