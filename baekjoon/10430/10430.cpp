/*
나머지 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%82%98%EB%A8%B8%EC%A7%80-%ED%92%80%EC%9D%B4
*/
#include <iostream>

using namespace std;
int main() {
	int A, B, C;
	cin >> A >> B >> C;
	cout << (A+B)%C<<'\n';
	cout << ((A%C)+(B%C))%C<<'\n';
	cout << (A*B)%C<<'\n';
	cout << ((A%C)*(B%C))%C;
}
