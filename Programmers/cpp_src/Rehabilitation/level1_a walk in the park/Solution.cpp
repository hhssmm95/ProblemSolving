#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<string> park, vector<string> routes) {
    vector<int> answer = {-1, -1};

    int n = park.size();
    int m = park[0].size();

    for(int i = 0; i<n; i++)
    {
        for(int j = 0; j<m; j++)
        {
            if(park[i][j] == 'S')
            {
                answer[0] = i;
                answer[1] = j;
                break;
            }
        }
        if(answer[0] != -1 && answer[1] != -1)
        {
            break;
        }
    }
    
    for(int i = 0; i<routes.size(); i++)
    {
        char dir = routes[i][0];
        int dist = routes[i][2] - '0';
        
        vector<int> desirePos(answer);

        while(dir == 'E' && dist > 0)
        {
            if(desirePos[1] + 1 < m && park[desirePos[0]][desirePos[1]+1] != 'X')
            {
                desirePos[1] += 1;
                --dist;
                
                if(dist == 0)
                    answer = desirePos;
            }
            else
                break;
        }
        while(dir == 'W' && dist > 0)
        {
            if(desirePos[1] - 1 >= 0 && park[desirePos[0]][desirePos[1]-1] != 'X')
            {
                desirePos[1] -= 1;
                --dist;
                
                if(dist == 0)
                    answer = desirePos;
            }
            else
                break;
        }
        while(dir == 'S' && dist > 0)
        {
            if(desirePos[0] + 1 < n && park[desirePos[0]+1][desirePos[1]] != 'X')
            {
                desirePos[0] += 1;
                --dist;
                
                if(dist == 0)
                    answer = desirePos;
            }
            else
                break;
        }
        while(dir == 'N' && dist > 0)
        {
            if(desirePos[0] - 1 >= 0 && park[desirePos[0]-1][desirePos[1]] != 'X')
            {
                desirePos[0] -= 1;
                --dist;
                
                if(dist == 0)
                    answer = desirePos;
            }
            else
                break;
        }
        
    }
    return answer;

//Brute Force 적용, 코드 최적화 필요
}