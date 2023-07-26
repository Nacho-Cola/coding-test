#include <vector>
using namespace std;

vector<int> qtree(vector<vector<int>> &arr){
    vector<int> answer(2,0);
    int s=arr.size();
    int zflag=1, oflag=1;
    for(int i=0 ; i<s; i++){
        for(int j=0 ; j<s; j++){
            if(arr[i][j]==0)oflag=0;
            if(arr[i][j]==1)zflag=0;   
        }
    }
    if(oflag){
        answer[1]++;
        return answer;
    }else if(zflag){
        answer[0]++;
        return answer;
    }else{
        vector<vector<int>> x1;
        vector<vector<int>> x2;
        vector<vector<int>> x3;
        vector<vector<int>> x4;
        for(int i =0; i<s ; i++){
            if(i<s/2){   
                x1.push_back(vector<int>(arr[i].begin(), arr[i].begin()+(s/2)));
                x2.push_back(vector<int>(arr[i].begin()+(s/2), arr[i].end()));
            }
            else{
                x3.push_back(vector<int>(arr[i].begin(), arr[i].begin()+(s/2)));
                x4.push_back(vector<int>(arr[i].begin()+(s/2), arr[i].end()));
            }
        }
        answer[0] = qtree(x1)[0] + qtree(x2)[0] + qtree(x3)[0] + qtree(x4)[0];
        answer[1] = qtree(x1)[1] + qtree(x2)[1] + qtree(x3)[1] + qtree(x4)[1];
    }
    return answer;
}

vector<int> solution(vector<vector<int>> arr) {
    return  qtree(arr);
}