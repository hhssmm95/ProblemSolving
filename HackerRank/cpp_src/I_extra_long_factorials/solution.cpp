#include <bits/stdc++.h>

using namespace std;

#define ll long long

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'extraLongFactorials' function below.
 *
 * The function accepts INTEGER n as parameter.
 */


string str_add_str(string a, string b)
{
	int len = max(a.size(), b.size());

	while (a.size() < len)
		a.insert(a.begin(), '0');

	while (b.size() < len)
		b.insert(b.begin(), '0');

	string total = "";

	int ceilNum = 0;
	for (int i = len-1; i >= 0; i--)
	{
		int added = (a[i] - '0') + (b[i] - '0') + ceilNum;
		ceilNum = added / 10;
		total = to_string(added % 10) + total;
		//total.insert(total.begin(), static_cast<char>(added % 10));
	}
	if(ceilNum > 0)
		total = to_string(ceilNum) + total;
	//total.insert(total.begin(), static_cast<char>(ceilNum));

	return total;
}

string str_mult_str(string a, string b)
{
	vector<string>sum_li;

	for (int i = b.size() - 1; i >= 0; i--)
	{
		string result = "";
		int ceilNum = 0;
		for (int j = a.size() - 1; j >= 0; j--)
		{
			int multied = (a[j] - '0')*(b[i] - '0') + ceilNum;
			ceilNum = multied / 10;
			result = to_string(multied % 10) + result;
			//result.insert(result.begin(), static_cast<char>(multied % 10));
		}
		if (ceilNum > 0)
			result = to_string(ceilNum) + result;
			//result.insert(result.begin(), static_cast<char>(ceilNum));

		for (int k = 0; k < b.size() - 1 - i; k++)
		{
			result.push_back('0');
		}

		sum_li.push_back(result);
	}

	string total = "";
	for (auto str_num : sum_li)
	{
		total = str_add_str(total, str_num);
	}

	return total;
}


void extraLongFactorials(int n) {
	vector<string> nums;

	for (int i = 1; i <= n; i++)
	{
		nums.push_back(to_string(i));
	}

	string result = nums[0];
	for (int i = 1; i<nums.size(); i++)
	{
		result = str_mult_str(result, nums[i]);
	}

	cout << result << endl;
}

int main()
{
	string n_temp;
	getline(cin, n_temp);

	int n = stoi(ltrim(rtrim(n_temp)));

	extraLongFactorials(n);

	return 0;
}

string ltrim(const string &str) {
	string s(str);

	s.erase(
		s.begin(),
		find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
	);

	return s;
}

string rtrim(const string &str) {
	string s(str);

	s.erase(
		find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
		s.end()
	);

	return s;
}
