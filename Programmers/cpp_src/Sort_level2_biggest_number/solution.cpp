#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(string a, string b)
{
	return a + b > b + a;
}

string solution(vector<int> numbers) {
	string answer = "";
	vector<string> strArray;


	for (auto num : numbers)
	{
		strArray.push_back(to_string(num));
	}

	sort(strArray.begin(), strArray.end(), cmp);

	if (strArray.at(0) == "0")
		return "0";

	for (auto str : strArray)
	{
		answer += str;
	}


	return answer;
}