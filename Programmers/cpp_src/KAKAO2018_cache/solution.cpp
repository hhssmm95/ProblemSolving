#include <string>
#include <vector>
#include <list>
#include <unordered_map>
#include <iostream>
using namespace std;

list<string> dq;
unordered_map<string, list<string>::iterator> ma;
int csize;



int refer(string x)
{
	int excute_time = 0;

	for (int i = 0; i < static_cast<int>(x.size()); i++)
	{
		if (x[i] >= 'A' && x[i] <= 'Z')
		{
			x[i] += 32;
		}
	}

	if (ma.find(x) == ma.end())
	{
		excute_time = 5;

		if (csize == 0)
		{
			return excute_time;
		}
		else if (dq.size() == csize)
		{
			string last = dq.back();
			dq.pop_back();
			ma.erase(last);
		}
	}

	else
	{
		dq.erase(ma[x]);
		excute_time = 1;
	}

	dq.push_front(x);
	ma[x] = dq.begin();
	return excute_time;
}


int solution(int cacheSize, vector<string> cities) {
	int answer = 0;
	csize = cacheSize;



	for (auto city_iter : cities)
	{
		answer += refer(city_iter);
	}

	return answer;
}

int main()
{
	vector<string> test_vector1 = { "Jeju", "Pangyo", "NewYork", "newyork" };//{9, 20, 28, 18, 11};

	int test_int1 = 2;


	cout << solution(test_int1, test_vector1) << endl;

	return 0;
}