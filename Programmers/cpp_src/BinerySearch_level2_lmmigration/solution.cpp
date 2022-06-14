#include <string>
#include <vector>
#include <algorithm>
using namespace std;


long long solution(int n, vector<int> times) {
	long long answer = 0;
	int m = times.size();
	long long start = 1;
	long long end = (long long)times.back()*n;
	long long mid = 0;

	sort(times.begin(), times.end());

	while (start <= end)
	{
		mid = (start + end) / 2;

		long long  cnt = 0;

		for (int i = 0; i < m; i++)
		{
			cnt += mid / times[i];
		}

		if (cnt < n)
		{
			start = mid + 1;
		}

		else
		{
			if (mid <= end)
				answer = mid;
			end = mid - 1;
		}
	}
	return answer;
}


int main()
{
	cout << solution(6, { 7,10 }) << endl;
	return 0;
}