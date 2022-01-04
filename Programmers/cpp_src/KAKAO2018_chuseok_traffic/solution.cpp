#include <string>
#include <vector>
#include <sstream>
#include <iostream>

using namespace std;

pair<int, int> LineToSecond(string line)
{
	istringstream ss(line);
	string ptime = "";
	string date = "";
	string time = "";

	ss >> date >> time >> ptime;
	vector<int>times = { stoi(time.substr(0,2)), stoi(time.substr(3, 2)),
	stoi(time.substr(6, 2)), stoi(time.substr(9,3)) };

	ptime.pop_back();

	int finish_as_second = 0;
	int ptime_as_second = 0;
	finish_as_second = times[0] * 3600 * 1000 + times[1] * 60 * 1000 + 
		times[2] * 1000 + times[3];

	int ondot = stoi(ptime.substr(0, 1)) * 1000;
	if (ptime[1] == '.')
	{
		int underdot = stoi(ptime.substr(2, ptime.size() - 2));
		ptime_as_second = ondot + underdot;
	}
	else
		ptime_as_second = ondot;

	float start_as_second = finish_as_second - (ptime_as_second - 1);

	return { start_as_second, finish_as_second};
}

int solution(vector<string> lines) {
	int answer = 0;

	vector<pair<int, int>> start_end_vector;
	for (auto line_iter : lines)
	{
		pair<int, int> start_end_pair = LineToSecond(line_iter);

		start_end_vector.push_back(start_end_pair);
	}

	int max = 0;

	for (int i = 0; i < start_end_vector.size(); i++)
	{
		int count = 1; 
		int SectorEnd = start_end_vector[i].second + 1000;

		for (int j = i + 1; j < start_end_vector.size(); j++)
		{
			if (start_end_vector[j].first < SectorEnd)
				count++;
		}
		if (count > max)
			max = count;
	}

	return max;

}


int main()
{
	vector<string> test_vector1 = { "2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s" };

	int result = solution(test_vector1);

	cout << result << endl;

	return 0;
}
