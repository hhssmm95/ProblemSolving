#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'nonDivisibleSubset' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER k
 *  2. INTEGER_ARRAY s
 
 s의 수를 포함해도 랜덤 두 수의 합이 k로 나누어떨어지지 않는경우 (정답 케이스)

 1. 집합 s 냐부에 k로 나눈 나머지가 0 수가 있는 경우 (정확하게 나누어 떨어지는 경우) -> 정답으로 하나만 포함 가능
 (2개 이상일 경우 나머지가 0인거끼리 더하면 k로 나누어떨어져버림)

 2. k가 짝수이고 집합 s 내부에 k로 나눈 나머지가 k/2 인 수가 있는 경우 -> 정답으로 하나만 포함 가능
 (2개 이상일 경우 나머지가 k/2인 수끼리 더하면 나머지가 0이 되어서 k로 나누어 떨어져버림)

 3. 나머지가 i인 경우와 k-i인 경우 중에선 둘 중에 한 케이스의 수만 포함할 수 있음
 (둘 다 포함할 경우 둘이 더해지는 경우에 나누어 떨어져버림, max(i,k-i) 이용하여 한 케이스만 포함할것
 */

int nonDivisibleSubset(int k, vector<int> s) {
	int answer = 0;
	vector<int> remainder_distrb(k,0); //각 수를 k로 나눈 나머지에 대한 분포도

	for (auto num : s)
		remainder_distrb[num%k]++;

	//위 조건의 1번
	answer += min(remainder_distrb[0], 1);

	//위 조건의 2번
	if (k % 2 == 0)
		answer += min(remainder_distrb[k / 2], 1);

	//위 조건의 3번
	for (int i = 1; i <= k / 2; i++)
	{
		//짝수인 경우 이미 위에서 2번 조건을 포함했으므로 중복 방지
		if (k % 2 == 0 && i == k / 2)
			continue;
		
		answer += max(remainder_distrb[i], remainder_distrb[k - i]);
	}

	return answer;

}

int main()
{
	ofstream fout(getenv("OUTPUT_PATH"));

	string first_multiple_input_temp;
	getline(cin, first_multiple_input_temp);

	vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

	int n = stoi(first_multiple_input[0]);

	int k = stoi(first_multiple_input[1]);

	string s_temp_temp;
	getline(cin, s_temp_temp);

	vector<string> s_temp = split(rtrim(s_temp_temp));

	vector<int> s(n);

	for (int i = 0; i < n; i++) {
		int s_item = stoi(s_temp[i]);

		s[i] = s_item;
	}

	int result = nonDivisibleSubset(k, s);

	fout << result << "\n";

	fout.close();

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

vector<string> split(const string &str) {
	vector<string> tokens;

	string::size_type start = 0;
	string::size_type end = 0;

	while ((end = str.find(" ", start)) != string::npos) {
		tokens.push_back(str.substr(start, end - start));

		start = end + 1;
	}

	tokens.push_back(str.substr(start));

	return tokens;
}
