#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

struct Node
{
	string parent;
	int money;

	Node(string p, int m):parent(p),money(m){}
};

unordered_map<string, Node*> parent_map;

void setNode(string child, string parent)
{
	if (parent == "-")
	{
		parent_map[child] = new Node("master", 0);
	}
	else
	{
		parent_map[child] = new Node(parent, 0);
	}
}

void sell(string name, int profit)
{
	if (parent_map[name]->parent == name)
	{
		parent_map[name]->money += profit;
		return;
	}

	int bonus = profit / 10;
	parent_map[name]->money += profit - bonus;

	if (bonus >= 1)
		sell(parent_map[name]->parent, bonus);

}

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
	vector<int> answer;
	int N = enroll.size();
	int M = seller.size();

	parent_map["master"] = new Node("master", 0);

	for (int i = 0; i < N; i++)
	{
		setNode(enroll[i], referral[i]);
	}

	for (int j = 0; j < M; j++)
	{
		sell(seller[j], amount[j]*100);
	}

	for (auto name : enroll)
		answer.push_back(parent_map[name]->money);

	return answer;

}

int main()
{

	/*vector<int> answer = solution({ "john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young" },
		{ "-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward" },
		{ "young", "john", "tod", "emily", "mary" }, { 12, 4, 2, 5, 10 });*/

	vector<int> answer = solution({ "john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young" },
		{ "-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward" },
		{ "sam", "emily", "jaimie", "edward" }, { 2, 3, 5, 4 });

	cout << "[";
	for (int i = 0; i<answer.size(); i++)
	{
		if (i < answer.size() - 1)
			cout << answer[i] << ", ";
		else
			cout << answer[i] << "]" << endl;
	}

	return 0;
}

/*
struct Node
{
	string name;
	int money;

	Node* base;
	unordered_map<string, Node*>derived;

	Node(string n, Node* b)
		:name(n), base(b) {
		money = 0;
	};

	Node() {
		name = "";
		money = 0;
		base = nullptr;
	};
};

unordered_map<string, int> result;

class ML_Tree
{
private:
	Node* root;

public:
	ML_Tree() {
		root = new Node();
		root->name = "master";
	}
	void add_Node(string n, string b)
	{
		if (b == "-")
			root->derived[n] = new Node(n, root);
		else
		{
			auto node = find(root, b);
			node->derived[n] = new Node(n, node);
		}
	}
	Node* find(Node* node, string fName)
	{
		if (!node->derived.empty())
		{
			if (node->derived.find(fName) == node->derived.end())
			{
				Node* temp = nullptr;
				for (auto derived_iter : node->derived)
				{
					 temp = find(derived_iter.second, fName);
					 if (temp != nullptr)
						 return temp;
				}

				return nullptr;
			}
			else
			{
				return node->derived[fName];
			}
		}
		else
		{
			return nullptr;
		}
	}

	void get_bonus(Node* node, int profit)
	{
		int bonus =  profit/10;
		node->money += profit - bonus;
		result[node->name] = node->money;

		if (bonus < 1 || node->base == nullptr)
			return;

		get_bonus(node->base, bonus);
	}

	void sale(string fName, int amount)
	{
		Node* seller = find(root, fName);
		int profit = amount * 100;
		int bonus = profit / 10;
		seller->money += profit - bonus;
		result[fName] = seller->money;

		if (bonus < 1 || seller->base == nullptr)
			return;

		get_bonus(seller->base, bonus);
	}
};

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
	vector<int> answer;
	ML_Tree tree;

	//init
	for (int i = 0; i < enroll.size(); i++)
	{
		tree.add_Node(enroll[i], referral[i]);
	}

	for (int i = 0; i < seller.size(); i++)
	{
		tree.sale(seller[i], amount[i]);
	}

	for (auto eName : enroll)
	{
		answer.push_back(result[eName]);
	}
	return answer;
}

*/