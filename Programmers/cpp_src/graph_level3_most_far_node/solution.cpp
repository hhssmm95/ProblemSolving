#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <limits>

using namespace std;

/*
n	vertex	return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3
*/
typedef pair<int, int> pii;

struct cmp_pii
{
	bool operator()(pii a, pii b)
	{
		return a.first < b.first;
	}
};

void dijkstra(int start, vector<int>& distances, vector<vector<pii>> graph)
{
	priority_queue < pii, vector<pii>, cmp_pii > pq;
	pq.push({ 0, start });
	distances[start] = 0;

	while (!pq.empty())
	{
		pii popped = pq.top();
		pq.pop();
		int curr_dist = popped.first;
		int curr_v = popped.second;

		if (distances[curr_v] < curr_dist)
			continue;

		for (auto p : graph[curr_v])
		{
			int next_v = p.first;
			int next_dist = p.second;

			int cost = curr_dist + next_dist;

			if (distances[next_v] > cost)
			{
				distances[next_v] = cost;
				pq.push({ cost, next_v });
			}
		}
	}
}

int solution(int n, vector<vector<int>> edge) {
	int answer = 0;
	vector<vector<pair<int, int>>> graph(n + 1);
	vector<int> distances(n+1, INT_MAX);
	distances[0] = -1;
	for (auto p : edge)
	{
		int v1 = p[0];
		int v2 = p[1];

		graph[v1].push_back({ v2,1 });
		graph[v2].push_back({ v1,1 });
	}

	dijkstra(1, distances, graph);

	int max_dist = -1;
	for (auto dist : distances)
	{
		if (max_dist < dist)
		{
			max_dist = dist;
			answer = 1;
		}
		else if (max_dist == dist)
			answer++;
	}


	return answer;
}

int main()
{
	cout << solution(6, { {3, 6},{4, 3},{3, 2},{1, 3},{1, 2},{2, 4},{5, 2} }) << endl;
}