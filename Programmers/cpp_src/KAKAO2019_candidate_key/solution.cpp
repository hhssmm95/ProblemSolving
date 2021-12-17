#include <vector>
#include <string>
#include <set>
#include <sstream>
#include <iostream>

using namespace std;
vector<string> keys;
int column = 0;
int row = 0;


void MakeKey(vector<string> origin_keys, string str, int idx, int depth)
{
	if (depth == origin_keys.size())
	{
		keys.push_back(str);
	}
	else
	{
		if (str.empty())
			MakeKey(origin_keys, str + origin_keys[idx], idx + 1, depth + 1);
		else
			MakeKey(origin_keys, str + " " + origin_keys[idx], idx + 1, depth + 1);

		MakeKey(origin_keys, str, idx + 1, depth + 1);
	}
}

bool CheckUniqueness(string key, vector<vector<string>> relation)
{
	stringstream ss(key);
	string str = "";
	vector<int> temp_key;
	while (ss >> str)
	{
		temp_key.push_back(stoi(str));
	}

	set<string> str_set;
	for (int i = 0; i < row; i++)
	{
		string s = "";
		for (int j = 0; j < temp_key.size(); j++)
		{
			s += relation[i][temp_key[j]];
		}

		if (str_set.find(s) != str_set.end())
			return false;
		else
			str_set.insert(s);
	}

	return true;

}
bool CheckMinimality(string key, vector<vector<string>> relation)
{
	stringstream ss(key);
	string str = "";
	vector<int> temp_key;
	int size = 0;
	while (ss >> str)
	{
		temp_key.push_back(stoi(str));
	}

	if (temp_key.size() == 1)
		return true;

	for (int i = 0; i < temp_key.size(); i++)
	{
		vector<int> key_copy = temp_key;
		key_copy.erase(key_copy.begin() + i);

		string s = "";
		for (int j = 0; j < key_copy.size(); j++)
		{
			if (j > 0)
				s += " ";
			s += to_string(key_copy[j]);
		}

		if (CheckUniqueness(s, relation))
			return false;
	}

	return true;
}

int solution(vector<vector<string>> relation) {
	int answer = 0;
	row = relation.size();
	column = relation[0].size();

	vector<string> origin_keys;

	for (int i = 0; i < column; i++)
	{
		origin_keys.push_back(to_string(i));
	}

	MakeKey(origin_keys, "", 0, 0);


	for (auto key_iter : keys)
	{
		if (CheckUniqueness(key_iter, relation) && CheckMinimality(key_iter, relation))
			answer++;
	}



	return answer;
}

//int main()
//{
//
//	vector<vector<string>> test_string1 = { {"100", "ryan", "music", "2"},{"200", "apeach", "math", "2"},
//	{"300", "tube", "computer", "3"},{"400", "con", "computer", "4"},
//		{"500", "muzi", "music", "3"},{"600", "apeach", "music", "2"} };
//
//	int result = solution(test_string1);
//
//	cout << result << endl;
//
//	cout << endl;
//	return 0;
//}
