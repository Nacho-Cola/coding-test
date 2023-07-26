#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> w) {
    vector<int> answer;
    vector<int>x;
    vector<int>y;
    for(int i=0; i<w.size();i++){
        for(int j=0; j<w[0].size(); j++){
            if(w[i][j] == '#'){
                x.push_back(i);
                y.push_back(j);
            }
        }
    }
    sort(x.begin(),x.end());
    sort(y.begin(),y.end());
    answer.push_back(x[0]);
    answer.push_back(y[0]);
    answer.push_back(x.back()+1);
    answer.push_back(y.back()+1);
    return answer;
}