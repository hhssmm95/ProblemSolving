#include <string>
#include <vector>
#include <queue>
#include<iostream>
#include<limits.h>

using namespace std;

#define DIR 4

int R[4] = { 1,-1,0,0 };
int C[4] = { 0,0,1,-1 };



int BFS(vector<vector<int>> board)
{
	int N = static_cast<int>(board.size());
	vector<vector<vector<int>>> visited(DIR, vector<vector<int>>(N, vector<int>(N, INT_MAX)));
	queue<vector<int>> bfsQ({ { 0,0,-1,0 } });

	while (!bfsQ.empty())
	{
		auto data = bfsQ.front();
		int r = data[0];
		int c = data[1];
		int dir = data[2];
		int cost = data[3];
		bfsQ.pop();

		for (int i = 0; i < DIR; i++)
		{
			int nr = r + R[i];
			int nc = c + C[i];

			if (0 <= nr && nr < N && 0 <= nc && nc < N)
			{
				if (board[nr][nc] == 1)
					continue;

				int nCost = cost + 100;
				
				if (dir != i && dir != -1)
					nCost += 500;

				if (visited[i][nr][nc] < nCost)
					continue;

				visited[i][nr][nc] = nCost;
				bfsQ.push({ nr,nc,i,nCost });
			}
		}
	}

	int min_cost = INT_MAX;
	for (int i = 0; i < DIR; i++)
	{
		if (min_cost > visited[i][N - 1][N - 1])
			min_cost = visited[i][N - 1][N - 1];
	}

	return min_cost;
			

}

int solution(vector<vector<int>> board) {
	int answer = BFS(board);
	return answer;
}

int main()
{
	cout << solution({ {0, 0, 0, 0, 0, 0, 0, 1}, {0, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 1, 0, 0}, {0, 0, 0, 0, 1, 0, 0, 0}, {0, 0, 0, 1, 0, 0, 0, 1}, {0, 0, 1, 0, 0, 0, 1, 0}, {0, 1, 0, 0, 0, 1, 0, 0}, {1, 0, 0, 0, 0, 0, 0, 0} });
}


/*
입출력 예
board	result
[[0,0,0],[0,0,0],[0,0,0]]	900
[[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]	3800
[[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]	2100
[[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]	3200
*/