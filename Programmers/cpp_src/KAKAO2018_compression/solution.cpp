#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;


vector<int> solution(string msg) 
{
	vector<int> answer;
	map<string, int> dict;
	int idx = 1;

	for (int i = 1; i<=26; i++)
	{
		string alphabet = "";
		alphabet += 'A' + (i - 1);
		dict.insert({ alphabet, i });
		idx++;
	}

	//buffer += msg[0];
	//answer.push_back(dict[buffer]);

	int count = 1;

	while (true)
	{
		string w = msg.substr(0, count);
		string c = msg.substr(count, 1);
		string wc = w + c;

		auto w_find = dict.find(w);
		auto c_find = dict.find(c);
		auto wc_find = dict.find(wc);

		if (w_find != dict.end())
		{
			if (wc_find != dict.end())
			{
				if (count < msg.size())
					count++;
			}
			else
			{
				answer.push_back(dict[w]);
				dict.insert({ wc, dict.size() + 1});
				msg.erase(0, count);
				count = 1;
			}
		}

		if (c == "\0")
		{
			answer.push_back(dict[w]);
			break;
		}

	}


	return answer;
}

int main()
{
	
	string test_string = "TOBEORNOTTOBEORTOBEORNOT";

	vector<int> result = solution(test_string);


	//string result = solution(test_string1);

	//cout << result << endl;

	for (auto result_iter : result)
	{
		cout << result_iter << " ";
	}
	cout << endl;
	return 0;
}