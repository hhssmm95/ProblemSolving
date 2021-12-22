#include <string>
#include <vector>
#include <set>

using namespace std;
set<pair<int, int>> visit_pair;

bool CheckTwoByTwo(int a, int b, vector<string> board)
{
	char block = board[a][b];

	if (a < board.size() - 1 && b < board[a].size() - 1 && board[a][b + 1] == block &&
		board[a + 1][b] == block && board[a + 1][b + 1] == block)
	{

		visit_pair.insert({ a,b });
		visit_pair.insert({ a,b + 1 });
		visit_pair.insert({ a+1,b});
		visit_pair.insert({ a+1,b + 1 });
		return true;
	}
	else
	{
		return false;
	}
}

int DeleteBlock(vector<string>& board)
{
	int count = 0;
	for (auto pair_iter : visit_pair)
	{
		board[pair_iter.first][pair_iter.second] = 'X';
		count++;
	}
	return count;
}

void DropBlock(int i, int j, vector<string>& board)
{
	int x = i;
	bool clean = false;

	while (board[x][j] == 'X')
	{
		if (x > 0)
			x--;
		else
		{
			clean = true;
			break;
		}
	}

	if (clean)
		return;

	board[i][j] = board[x][j];
	board[x][j] = 'X';
}


int solution(int m, int n, vector<string> board) {
	int answer = 0;
	bool flag = true;

	while (flag)
	{
		flag = false;
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (board[i][j] != 'X' && CheckTwoByTwo(i, j, board))
				{
					flag = true;
				}
			}
		}

		if (flag)
		{
			answer += DeleteBlock(board);

			for (int j = 0; j < n; j++)
			{
				for (int i = m - 1; i > 0; i--)
				{
					if (board[i][j] == 'X')
					{
						DropBlock(i, j, board);
					}
				}
			}

			visit_pair.clear();
		}
		else
			break;
	}

	

	return answer;
}