#include <vector>
#include <string>
#include <iostream>
#include <queue>

using namespace std;

int R[4] = { 1,-1, 0, 0 };
int C[4] = { 0,0,1,-1 };

int BFS(int m, int n, vector<vector<int>> picture, vector<vector<bool>>& visited, pair<int,int> pos)
{
	queue<pair<int, int>> q;
	q.push(pos);

	int count = 1;
	int color = picture[pos.first][pos.second];

	while (!q.empty())
	{
		int r = q.front().first;
		int c = q.front().second;
		q.pop();


		for (int i = 0; i < 4; i++)
		{
			int nr = r + R[i];
			int nc = c + C[i];

			if (nr >= 0 && nr < m && nc >= 0 && nc < n)
			{
				if (visited[nr][nc] == false and picture[nr][nc] == color)
				{
					visited[nr][nc] = true;
					q.push({ nr,nc });
					++count;
				}

			}
		}
	}

	return count;
}

vector<int> solution(int m, int n, vector<vector<int>> picture)
{
	vector<vector<bool>> visited(m, vector<bool>(n, false));
	vector<int> answer(2,0);

	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (visited[i][j] == false && picture[i][j] > 0)
			{
				visited[i][j] = true;
				++answer[0];

				int width = BFS(m, n, picture, visited, { i,j });
				if (width > answer[1])
					answer[1] = width;
			}
		}
	}
	return answer;
}

int main()
{
	vector<int>result = solution(6, 4, { {1, 1, 1, 0},{1, 2, 2, 0},{1, 0, 0, 1},{0, 0, 0, 1},{0, 0, 0, 3},{0, 0, 0, 3} });

	cout << result[0] <<" "<< result[1] << endl;
}
