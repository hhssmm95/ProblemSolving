#include <string>
#include <vector>
#include <iostream>

using namespace std;

void rotateKey(vector<vector<int>>& key)
{
	int n = key.size();

	// reverse up and down
	for (int i = 0; i < n / 2; i++) 
	{
		for (int j = 0; j < n; j++) 
		{
			int temp = key[i][j];
			key[i][j] = key[n - i - 1][j];
			key[n - i - 1][j] = temp;

		}
	}

	// reverse diagonally
	for (int i = 0; i < n; i++) 
	{
		for (int j = i; j < n; j++) 
		{
			int temp = key[i][j];
			key[i][j] = key[j][i];
			key[j][i] = temp;
		}
	}
}

vector<vector<vector<int>>> makeKeys(vector<vector<int>> key)
{
	vector<vector<vector<int>>> keys;
	keys.push_back(key);

	for (int i = 0; i < 3; i++)
	{
		rotateKey(key);
		keys.push_back(key);
	}

	return keys;
}
bool correctCheck(vector<vector<int>> board, int M, int N)
{
	for (int j = 0; j < N; j++)
	{
		for (int k = 0; k < N; k++)
		{
			if (board[M - 1 + j][M - 1 + k] == 0)
				return false;
		}
	}

	return true;
}


bool solve(vector<vector<vector<int>>> keys, vector<vector<int>> lock, int N, int M)
{
	for (int x_offset = 0; x_offset < M - 1 + N; x_offset++)
	{
		for (int y_offset = 0; y_offset < M - 1 + N; y_offset++)
		{
			//check through each 90degree rotation
			for (int i = 0; i < keys.size(); i++)
			{
				vector<vector<int>> board(N + M * 2 - 2, vector<int>(N + M * 2 - 2, 1));

				//init lock
				for (int j = 0; j < N; j++)
				{
					for (int k = 0; k < N; k++)
					{
						if (lock[j][k] == 0)
						{
							board[M - 1 + j][M - 1 + k] = lock[j][k];
						}
					}
				}

				//init key
				bool available = true;
				for (int j = 0; j < M; j++)
				{
					if (j + x_offset < M - 1 || j + x_offset > M - 1 + N - 1)
						continue;
					for (int k = 0; k < M; k++)
					{
						if (k + y_offset < M - 1 || k + y_offset > M - 1 + N - 1)
							continue;

						if (board[j + x_offset][k + y_offset] == 0)
							board[j + x_offset][k + y_offset] = keys[i][j][k];

						else if (board[j + x_offset][k + y_offset] == 1 && keys[i][j][k] == 1)
							available = false;
					}
				}

				if (available && correctCheck(board, M, N))
					return true;
			}
		}
	}

	return false;
}


bool solution(vector<vector<int>> key, vector<vector<int>> lock) 
{
	bool answer = false;
	int N = lock.size();
	int M = key.size();
	
	vector<vector<vector<int>>> keys = makeKeys(key);

	if (solve(keys, lock, N, M))
		answer = true;
	

	return answer;
}

int main()
{
	vector<vector<int>> key = { {0, 0, 0},{1, 0, 0},{0, 1, 1} };
	vector<vector<int>> lock = { {1, 1, 1},{1, 1, 0},{1, 0, 1} };

	string result = "";
	if (solution(key, lock))
		result = "true";
	else
		result = "false";

	cout << result << endl;

	return 0;
}