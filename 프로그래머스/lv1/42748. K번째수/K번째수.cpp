#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for (const auto& command : commands) {
        int i = command[0];
        int j = command[1];
        int k = command[2];

        vector<int> sliced_array(array.begin() + i - 1, array.begin() + j); 
        sort(sliced_array.begin(), sliced_array.end()); 
        answer.push_back(sliced_array[k - 1]);
    }
    return answer;
}
