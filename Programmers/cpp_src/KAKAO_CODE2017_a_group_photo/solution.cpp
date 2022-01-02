#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool ConditionCheck(string position, vector<string> data)
{
	for (auto cond_iter : data)
	{
		char from = cond_iter[0];
		char target = cond_iter[2];
		char oper = cond_iter[3];
		int num = cond_iter[4] - '0';

		switch (oper)
		{
		case '=':
			if (abs(find(position.begin(), position.end(), from) -
				find(position.begin(), position.end(), target)) - 1 != num)
				return false;
			break;

		case '<':
			if (abs(find(position.begin(), position.end(), from) -
				find(position.begin(), position.end(), target)) - 1 >= num)
				return false;
			break;

		case '>':
			if (abs(find(position.begin(), position.end(), from) -
				find(position.begin(), position.end(), target)) - 1 <= num)
				return false;
			break;
		}

	}

	return true;
}

int friends_permutation(string position, vector<string> data)
{
	int count = 0;

	sort(position.begin(), position.end());
	do
	{
		if (ConditionCheck(position, data))
			count++;

	} while (next_permutation(position.begin(), position.end()));

	return count;

}

int solution(int n, vector<string> data) {
	int answer = 0;

	answer = friends_permutation("ACFJMNRT", data);


	return answer;
}

int main()
{
	int test_int1 = 2;
	vector<string> test_vector1 = { "M~C<2", "C~M>1" };

	int result = solution(test_int1, test_vector1);

	cout << result << endl;

	return 0;
}