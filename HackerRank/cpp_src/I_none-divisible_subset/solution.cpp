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
 
 s�� ���� �����ص� ���� �� ���� ���� k�� ����������� �ʴ°�� (���� ���̽�)

 1. ���� s �ĺο� k�� ���� �������� 0 ���� �ִ� ��� (��Ȯ�ϰ� ������ �������� ���) -> �������� �ϳ��� ���� ����
 (2�� �̻��� ��� �������� 0�ΰų��� ���ϸ� k�� �������������)

 2. k�� ¦���̰� ���� s ���ο� k�� ���� �������� k/2 �� ���� �ִ� ��� -> �������� �ϳ��� ���� ����
 (2�� �̻��� ��� �������� k/2�� ������ ���ϸ� �������� 0�� �Ǿ k�� ������ ����������)

 3. �������� i�� ���� k-i�� ��� �߿��� �� �߿� �� ���̽��� ���� ������ �� ����
 (�� �� ������ ��� ���� �������� ��쿡 ������ ����������, max(i,k-i) �̿��Ͽ� �� ���̽��� �����Ұ�
 */

int nonDivisibleSubset(int k, vector<int> s) {
	int answer = 0;
	vector<int> remainder_distrb(k,0); //�� ���� k�� ���� �������� ���� ������

	for (auto num : s)
		remainder_distrb[num%k]++;

	//�� ������ 1��
	answer += min(remainder_distrb[0], 1);

	//�� ������ 2��
	if (k % 2 == 0)
		answer += min(remainder_distrb[k / 2], 1);

	//�� ������ 3��
	for (int i = 1; i <= k / 2; i++)
	{
		//¦���� ��� �̹� ������ 2�� ������ ���������Ƿ� �ߺ� ����
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
