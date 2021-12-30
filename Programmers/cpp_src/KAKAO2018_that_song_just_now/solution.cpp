#include <string>
#include <vector>
#include <map>
#include <iostream>

using namespace std;

map<string, char> sharp_map = { {"C#", 'c'}, {"D#", 'd'}, {"F#", 'f'}, {"G#", 'g'}, {"A#", 'a'} };

string Change(string s)
{
	string result = "";

	for (int i = 0; i < s.size(); i++)
	{
		if (s[i] == '#')
		{
			string str = "";
			str += s[i - 1];
			str += s[i];
			result[result.size()-1] = sharp_map[str];
		}
		else
			result += s[i];
	}

	return result;
}

pair<string, int> CompareInfo(string m, string info)
{
	vector<string> infos;

	

	string buffer = "";
	for (int i = 0; i < info.size(); i++)
	{
		if (info[i] == ',')
		{
			infos.push_back(buffer);
			buffer.clear();
		}
		else
		{
			buffer += info[i];
		}
	}
	infos.push_back(buffer);

	string start_time = infos[0];
	string end_time = infos[1];
	string title = infos[2];
	string sheet = infos[3];


	sheet = Change(sheet);

	int start_minute = stoi(start_time.substr(0, 2)) * 60 + stoi(start_time.substr(3, 2));
	int end_minute = stoi(end_time.substr(0, 2)) * 60 + stoi(end_time.substr(3, 2));
	int playtime = end_minute - start_minute;

	string str = sheet;

	while (str.size() < playtime)
		str += sheet;

	str = str.substr(0, playtime);

	if(str.find(m) != str.npos)
		return { title, playtime };
	else
		return { "(None)", playtime };
}

string solution(string m, vector<string> musicinfos) {
	string answer = "(None)";
	int max_playtime = 0;
	m = Change(m);

	for (auto info_iter : musicinfos)
	{
		pair<string, int> result = CompareInfo(m, info_iter);
		if (result.first != "(None)" && result.second > max_playtime)
		{
			max_playtime = result.second;
			answer = result.first;
		}
	}


	return answer;
}