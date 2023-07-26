#include <string>
#include <vector>

using namespace std;

string solution(vector<string> cards1, vector<string> cards2, vector<string> goal) {
    int sp1=0, sp2=0;
    for(string s: goal){
        if(s==cards1[sp1]){
            sp1+=1;
        }
        else if(s==cards2[sp2]){
            sp2+=1;
        }
        else{
            return "No";
        }
            
    }
    return "Yes";
}