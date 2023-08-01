#include <string>
#include <vector>

using namespace std;
string solution(int a, int b) {
    vector<string> answer = {"THU","FRI","SAT","SUN","MON","TUE","WED"};
    vector<int>days = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int sum =0;
    for(int i=0 ; i<a-1 ; i++){
        sum+=days[i];
    }
    return answer[(sum+b)%7];
}