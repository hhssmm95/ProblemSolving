#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    vector<int> answer;
    
    unordered_map<string,int> name_map;
    
    for(int i = 0; i<name.size(); i++)
    {
        name_map.insert({name[i], yearning[i]});
    }
    
    for(int i = 0; i<photo.size(); i++)
    {
        answer.push_back(0);
        for(int j = 0; j<photo[i].size(); j++)
        {
            answer[answer.size()-1] += name_map[photo[i][j]];
        }
    }
    
    
    return answer;
}