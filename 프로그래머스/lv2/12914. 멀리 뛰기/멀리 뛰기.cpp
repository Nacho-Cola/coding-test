#include <iostream>

using namespace std;

const int MOD = 1234567;

int solution(int n) {
    if(n==1)
        return 1;
    int prev = 1;
    int cur = 2;
    for (int i = 3; i <= n; i++) {
        int next = (prev + cur) % MOD;
        prev = cur;
        cur = next;
    }
    return cur;
}
