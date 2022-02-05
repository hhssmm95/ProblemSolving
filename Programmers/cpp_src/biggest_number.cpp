#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

using namespace std;

string solution(vector<int> numbers) 
{
    vector<int> answer;
    sort(numbers.begin(), numbers.end());
    cout<<sum(numbers)<<endl;

    // do
    // {
    // } while (next_permutation(numbers.begin(), numbers.end()));
    return "";
        
}

int main()
{
    solution({1,2,3});
}