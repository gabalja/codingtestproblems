/*
사칙연산 C++ 풀이
https://www.acmicpc.net/problem/10869
*/
#include <iostream>

using namespace std;
int main() {
	int first, second;
	cin >> first >> second;
    cout << first+second<<'\n';
	cout << first-second<<'\n';
	cout << first*second<<'\n';
	cout << first/second<<'\n';
	cout << first%second;
}
