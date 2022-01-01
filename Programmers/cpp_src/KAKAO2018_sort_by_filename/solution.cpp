#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;



string GetHead(string file)
{
	string head = "";
	for (int i = 0; i < file.size(); i++)
	{
		if (file[i] >= '0' && file[i] <= '9')
		{
			return head;
		}
		else
		{
			if (file[i] >= 'A' && file[i] <= 'Z')
				head += file[i] + 32;
			else
				head += file[i];
		}
	}
}

string GetNumber(string file)
{
	string Number = "";
	bool flag = false;
	for (int i = 0; i < file.size(); i++)
	{
		if (!flag && (file[i] >= '0' && file[i] <= '9'))
		{
			flag = true;
		}

		if (flag && (file[i] >= '0' && file[i] <= '9'))
		{
			Number += file[i];
		}
		else if (flag && (file[i] < '0' || file[i] > '9'))
			return Number;
	}
}
bool CompareHead(string a, string b)
{
	if (GetHead(a) == GetHead(b))
	{
		return stoi(GetNumber(a)) < stoi(GetNumber(b));
	}
	else
		return GetHead(a) < GetHead(b);
}
vector<string> solution(vector<string> files) {
	stable_sort(files.begin(), files.end(), CompareHead);

	return files;
}

int main()
{
	vector<string> test_vector1 = { "F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat" };


	vector<string> result = solution(test_vector1);


	for (auto result_iter : result)
	{
		cout << result_iter << " ";
	}
	cout << endl;
	return 0;
}
