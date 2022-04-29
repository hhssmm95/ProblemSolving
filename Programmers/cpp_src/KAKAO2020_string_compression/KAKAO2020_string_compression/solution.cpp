#include <vector>
#include <string>
#include <iostream>

using namespace std;
int solution(string s)
{
	if (s.size() == 1)
		return 1;

	int min_len = 1001;
	for (int div = 1; div < s.size() / 2 + 1; div++)
	{
		string result = "";
		int count = 0;
		string str = s.substr(0, div);
		for (int i = 0; i < s.size(); i++)
		{
			if (s.substr(i, div) == str)
			{
				++count;
				i += div - 1;
			}
			else
			{
				if (count > 1)
				{
					result += to_string(count) + str;
				}
				else
				{
					result += str;
				}
				count = 0;
				str = s.substr(i, div);
				i -= 1;
			}

		}

		if (count > 1)
		{
			result += to_string(count) + str;
		}
		else
		{
			result += str;
		}

		if (min_len > result.size())
		{
			min_len = result.size();
		}

	}

	return min_len;
}


int main()
{
	string test_string1 = "x";
	cout << solution(test_string1) << endl;

	return 0;
}