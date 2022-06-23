#include <vector>
#include <iostream>

using namespace std;

int R[4] = { 1, 0, 1, 1 };
int C[4] = { 0, 1, 1,-1 };
int minR = 19;
int minC = 19;


bool checkWin(vector<vector<int>> board, vector<vector<bool>>& visited, int N, int M,
	pair<int, int> pos, int color)
{
	int r = pos.first;
	int c = pos.second;
	for (int dir = 0; dir < 4; dir++)
	{
		for (int i = 0; i < 6; i++)
		{
			int startR = r - (R[dir] * i);
			int startC = c - (C[dir] * i);

			if (startR < 0 || N <= startR || startC < 0 || M <= startC || board[startR][startC] != color || visited[startR][startC])
				break;

			int count = 1;

			for (int j = 1; j < 6; j++)
			{
				int nr = startR + (R[dir] * j);
				int nc = startC + (C[dir] * j);

				if (nr < 0 || N <= nr || nc < 0 || M <= nc || board[nr][nc] != color || visited[nr][nc])
					break;
				else
					count++;
			}
			if (count == 5)
			{
				
				int prevR = startR - R[dir];
				int prevC = startC - C[dir];
				if (prevR < 0 || N <= prevR || prevC < 0 || M <= prevC || board[prevR][prevC] != color)
				{
					if (dir == 3)
					{
						minR = startR + (R[dir] * 4);
						minC = startC + (C[dir] * 4);
					}
					else
					{
						minR = startR;
						minC = startC;
					}
					return true;
				}
			}
		}
	}

	return false;
}


void solution(vector<vector<int>> board)
{
	int N = board.size();
	int M = board[0].size();
	vector<vector<bool>> visited(N, vector<bool>(M, false));

	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			if (board[i][j] != 0 && visited[i][j] == false)
			{
				if (checkWin(board, visited, N, M, { i,j }, board[i][j]))
				{
					cout << board[i][j] << endl;
					cout << minR + 1 << " " << minC + 1 << endl;
					return;
				}

				visited[i][j] = true;

			}
		}
	}

	cout << 0 << endl;

}


int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	vector<vector<int>> board(19, vector<int>(19, -1));

	for (int i = 0; i < 19; i++)
	{
		for (int j = 0; j < 19; j++)
		{
			cin >> board[i][j];
		}
	}

	solution(board);
	

	return 0;
}