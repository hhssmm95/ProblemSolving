#include <iostream>
#include<string>
#include<queue>
#include<stack>

using namespace std;

int solution(string s)
{
	stack<char>cStack;
	deque<char>cDeque;
	
	for (auto c : s)
		cDeque.push_back(c);

	while (!cDeque.empty())
	{
		cStack.push(cDeque.front());
		cDeque.pop_front();

		while (!cStack.empty() && !cDeque.empty() && cStack.top() == cDeque.front())
		{
			cStack.pop();
			cDeque.pop_front();

			if (cStack.empty() && cDeque.empty())
				return true;
		}

	}
	

	return false;
}

int main()
{
	cout<<solution("baabaa")<<endl;
}