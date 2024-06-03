#include <string>
#include <vector>

using namespace std;

/*
[".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]	[0, 0, 7, 9]
*/

vector<int> solution(vector<string> wallpaper) {

    int v = wallpaper.size();
    int h = wallpaper[0].size();
    vector<int> answer = {v,h,-1,-1};

    
    // int top = v;
    // int left = h;
    // int right = -1;
    // int bottom = -1;
    
    for(int i = 0; i < v; i++)
    {
        for(int j = 0; j < h; j++)
        {
            if(wallpaper[i][j] != '#')
            {
                continue;
            }

            if(i < answer[0])
            {
                answer[0] = i;
            }

            if(i > answer[2])
            {
                answer[2] = i;
            }

            if(j < answer[1])
            {
                answer[1] = j;
            }

            if(j > answer[3])
            {
                answer[3] = j;
            }

        }
    }

    answer[2]++;
    answer[3]++;
    
    return answer;
}

int main()
{
    solution({".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."});

    return 0;
}