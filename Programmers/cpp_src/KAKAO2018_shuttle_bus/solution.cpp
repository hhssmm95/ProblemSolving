#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int timeToMinute(string time)
{
	int hour = stoi(time.substr(0,2));
	int minute = stoi(time.substr(3,2));

	return hour * 60 + minute;
}

string minuteToTime(int time)
{
	int hour = time / 60;
	int minute = time % 60;

	string str = "";
	if (hour < 10)
		str += "0" + to_string(hour);
	else
		str += to_string(hour);

	str += ":";

	if (minute < 10)
		str += "0" + to_string(minute);
	else
		str += to_string(minute);

	return str;
}

string solution(int n, int t, int m, vector<string> timetable) {
	int tableIdx = 0;

	sort(timetable.begin(), timetable.end());

	for (int i = 0; i < n; i++)
	{
		int time = 540 + t * i;
		vector<int> line;

		for (int j = tableIdx; j < timetable.size(); j++)
		{
			if (timeToMinute(timetable[j]) <= time && line.size() < m)
			{
				line.push_back(timeToMinute(timetable[j]));
				tableIdx = j + 1;
				if (line.size() == m)
					break;
			}
		}

		if (i == n - 1 && line.size() < m)
		{
			return minuteToTime(time);
		}
	}

}

int main()
{
	int n = 2;
	int t = 10;
	int m = 2;

	vector<string> timetable = { "09:10", "09:09", "08:00" };

	string result = solution(n, t, m, timetable);
	cout << result << endl;
}