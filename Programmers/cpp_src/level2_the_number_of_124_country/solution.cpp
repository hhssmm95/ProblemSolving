#include <vector>
#include <string>
#include <iostream>

using namespace std;


string get_radix_124(int dec)
{
	string result = "";
	int N = 3;

	if (dec < 3)
	{
		return to_string(dec);
	}
	if (dec == 3)
		return "4";
	
	while (dec >= 3)
	{
		int remain = dec % 3;

		char curr_char = ' ';

		if (remain == 0)
			curr_char = '4';
		else
			curr_char = static_cast<char>(remain + 48);

		result.insert(result.begin(), curr_char);
		dec /= 3;
		if (remain == 0)
			dec -= 1;
	}
	if (dec > 0)
	{
		char curr_char = ' ';

		
		curr_char = static_cast<char>(dec + 48);
		result.insert(result.begin(), curr_char);
	}

	return result;
}

string solution(int n) {
	string answer = get_radix_124(n);
	return answer;
}

int main()
{
	for (int i = 1; i < 31; i++)
	{
		string answer = solution(i);
		for (auto s : answer)
			cout << s;
		cout << endl;
	}
	return 0;
}