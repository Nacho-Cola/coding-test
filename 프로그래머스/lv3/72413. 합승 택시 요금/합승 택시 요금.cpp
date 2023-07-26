#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    vector<int> answer;
    vector<int> arr(n,1000000);
    vector<vector<int>> map(n,arr);
    
    for(int i=0; i<fares.size(); i++){
        if(i<n)
            map[i][i] = 0;
        map[fares[i][0]-1][fares[i][1]-1] = fares[i][2];
        map[fares[i][1]-1][fares[i][0]-1] = fares[i][2];
    }
    
    for(int k = 0; k < n; k++){
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if (map[i][k] + map[k][j] <= map[i][j]){
                    map[i][j] = map[i][k] + map[k][j];
                }
            }
        }
    } 
    
    for(int i = 0; i < n; i++){
        answer.push_back(map[s-1][i]+map[i][a-1]+map[i][b-1]);
    }
    
    
    return *min_element(answer.begin(), answer.end());
}