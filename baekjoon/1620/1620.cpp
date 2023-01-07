/*
나는야 포켓몬 마스터 이다솜 C++ 풀이
https://doctcoder.tistory.com/entry/%EB%82%98%EB%8A%94%EC%95%BC-%ED%8F%AC%EC%BC%93%EB%AA%AC-%EB%A7%88%EC%8A%A4%ED%84%B0-%EC%9D%B4%EB%8B%A4%EC%86%9C-%ED%92%80%EC%9D%B4
*/
#include <iostream>
#include <string.h>
#include <map>
using namespace std;
int main(void)
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    map<int, string> mpInt;
    map<string, int> mpStr;
    int n, m, idx = 0;
    cin >> n >> m;
    while (n--)
    {
        idx++;
        string str;
        cin >> str;
        mpInt.insert(make_pair(idx, str));
        mpStr.insert(make_pair(str, idx));
    }
    while (m--)
    {
        char arr[21];
        cin >> arr;
        if (isdigit(arr[0]))
        {
            int intArr = atoi(arr);
            cout << mpInt.find(intArr)->second << "\n";
        }
        else
        {
            cout << mpStr.find(arr)->second << "\n";
        }
    }
}
