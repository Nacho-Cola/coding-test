#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string s) {
    vector<int> str;
    string answer = "";
    str.push_back(stoi(s));
    
    for (int i = 0; i < s.size() ; i++) {
        if (s[i] == ' ') {
            str.push_back(stoi(&s[i]));
        }
    }
    sort(str.begin(), str.end());
    
    answer.append(to_string(str.front()));
    answer.push_back(' ');
    answer.append(to_string(str.back()));
    
    return answer;
}