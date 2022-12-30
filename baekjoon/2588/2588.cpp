/*
곱셈 C++ 풀이
https://doctcoder.tistory.com/entry/%EA%B3%B1%EC%85%88-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main() {
	int a, b;
	cin >> a >> b;
	cout<<a*(b%10)<<'\n'; // 1의 자리수
	cout<<a*((b/10)%10)<<'\n'; // 10의 자리수
	cout<<a*(b/100)<<'\n'; // 100의 자리수
	cout<<a*b;
}
