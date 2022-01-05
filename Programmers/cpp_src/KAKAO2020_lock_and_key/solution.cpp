#include <string>
#include <vector>

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
		keys.push_back(key);
	}

	return keys;
}

bool solution(vector<vector<int>> key, vector<vector<int>> lock) 
{
	bool answer = true;
	int N = lock.size();
	int M = key.size();
	vector<vector<int>> board(N + M * 2 - 2, vector<int>(N + M * 2 - 2, 0));
	vector<vector<vector<int>>> keys = makeKeys(key);

	

	return answer;
}