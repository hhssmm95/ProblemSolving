#include <string>
#include <vector>
#include <iostream>

using namespace std;

int N = 10;  //radix num

string Radix_N_Calculate(int dec)
{
	string result = "";

	if (dec == 0)
		return "0";

	while (dec >= N)
	{
		int remain = dec % N;

		if(remain >= 10)
			result.insert(result.begin(), static_cast<char>('A' + remain - 10));
		else
			result.insert(result.begin(), static_cast<char>(remain + 48));

		dec /= N;
	}
	if (dec > 0)
	{
		if (dec >= 10)
			result.insert(result.begin(), static_cast<char>('A' + dec - 10));
		else
			result.insert(result.begin(), static_cast<char>(dec + 48));
	}

	return result;
}

string solution(int n, int t, int m, int p) 
{
	string answer = "";
	
	int num = 0;
	int seq = 1;

	N = n;

	while (answer.size() < t)
	{
		string current_radix = "";

		current_radix = Radix_N_Calculate(num++);
		if (current_radix.size() >= 2)
		{
			for (int i = 0; i < current_radix.size(); i++)
			{
				if (seq == p)
				{
					answer += current_radix[i];
					if (answer.size() == t)
						return answer;
				}

				seq++;
				if (seq > m)
					seq = 1;
			}
		}
		else
		{
			if (seq == p)
			{
				answer += current_radix;
			}

			seq++;
			if (seq > m)
				seq = 1;
		}
	}

	return answer;
}

int main()
{
	
	int test_int1 = 16;
	int test_int2 = 16;
	int test_int3 = 2;
	int test_int4 = 2;


	string result = solution(test_int1, test_int2, test_int3, test_int4);

	cout << result << endl;

	return 0;
}