//#include<bits/stdc++.h>
#include <vector>
#include <string>
#include <stack>
#include<iostream>

using namespace std;

struct Node
{
	int data;
	Node* prevNode;
	Node* nextNode;

	Node(int n)
	{
		data = n;
		prevNode = nullptr;
		nextNode = nullptr;
	}
};



unordered_map<int, pair<int, list<int>::iterator>> delMap;

void processOrder(string order, Node*& LL,
	Node*& select, stack<Node*>& delStack, string& answer)
{
	string ord = order.substr(0, 1);
	int val = 0;
	if (order.size() > 1)
		val = stoi(order.substr(2, order.size() - 2));


	if (ord == "U")
	{
		while (val > 0)
		{
			select = select->prevNode;
			val -= 1;
		}
	}
	else if (ord == "D")
	{
		while (val > 0)
		{
			select = select->nextNode;
			val -= 1;
		}
	}
	else if (ord == "C")
	{
		delStack.push(select);
		answer[select->data] = 'X';

		//if select node is head
		if (select->prevNode == nullptr)
		{
			LL = select->nextNode;
			LL->prevNode = nullptr;
			select = select->nextNode;
		}
		//if select node is tail
		else if (select->nextNode == nullptr)
		{
			select->prevNode->nextNode = nullptr;
			select = select->prevNode;
		}
		else
		{
			select->prevNode->nextNode = select->nextNode;
			select->nextNode->prevNode = select->prevNode;
			select = select->nextNode;
		}
	}
	else
	{
		//if top is head
		if (delStack.top()->prevNode == nullptr)
		{
			LL = delStack.top();
			auto next = delStack.top()->nextNode;
			next->prevNode = delStack.top();
		}
		//if top is tail
		else if (delStack.top()->nextNode == nullptr)
		{
			auto prev = delStack.top()->prevNode;
			prev->nextNode = delStack.top();
		}
		else
		{
			auto prev = delStack.top()->prevNode;
			prev->nextNode = delStack.top();
			auto next = delStack.top()->nextNode;
			next->prevNode = delStack.top();
		}
		answer[delStack.top()->data] = 'O';
		delStack.pop();
	}
}

void clearLL(Node*& currNode)
{
	if (currNode->nextNode != nullptr)
		clearLL(currNode->nextNode);
	delete currNode;
}

void clearStack(stack<Node*> delStack)
{
	while (!delStack.empty())
	{
		delete delStack.top();
		delStack.pop();
	}
}

string solution(int n, int k, vector<string> cmd) {
	string answer(n, 'O');
	Node* LL = new Node(0);
	Node* select = LL;
	stack<Node*> delStack;

	for (int i = 1; i < n; i++)
	{
		select->nextNode = new Node(i);
		select->nextNode->prevNode = select;
		select = select->nextNode;
	}
	
	select = LL;
	for (int i = 0; i < k; i++)
	{
		select = select->nextNode;
	}

	for (auto order : cmd)
	{
		processOrder(order, LL, select, delStack, answer);
	}

	
	clearLL(LL);
	clearStack(delStack);
	return answer;
}

int main()
{
	cout << solution(8, 2, { "D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C" }) << endl;
	

	return 0;

}