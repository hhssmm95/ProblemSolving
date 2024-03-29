#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

/*
문제 설명
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

제한사항
전체 학생의 수는 2명 이상 30명 이하입니다.
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
입출력 예
n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	4
3	[3]	[1]	2
입출력 예 설명
예제 #1
1번 학생이 2번 학생에게 체육복을 빌려주고, 3번 학생이나 5번 학생이 4번 학생에게 체육복을 빌려주면 학생 5명이 체육수업을 들을 수 있습니다.

예제 #2
3번 학생이 2번 학생이나 4번 학생에게 체육복을 빌려주면 학생 4명이 체육수업을 들을 수 있습니다.
*/

int solution(int n, vector<int> lost, vector<int> reserve) {
    
    int answer = n;

    


    unordered_set<int> r_set;
    unordered_set<int> l_set;

    
    for(const auto r_num : reserve)
    {
        r_set.insert(r_num);
    }
    for(const auto l_num : lost)
    {
        l_set.insert(l_num);
    }

    for(int i = 1; i<n+1; i++)
    {
        if(r_set.find(i) != r_set.end() && l_set.find(i) != l_set.end())
        {
            r_set.erase(i);
            l_set.erase(i);
        }
    }

    // vector<int> new_lost;
    // for(const auto l_num : l_set)
    // {
    //     new_lost.push_back(l_num);
    // }

    vector<int> new_reserve;
    for(const auto r_num : r_set)
    {
        new_reserve.push_back(r_num);
    }

    //sort(new_lost.begin(), new_lost.end());
    sort(new_reserve.begin(), new_reserve.end());

    for(const auto nr_num : new_reserve)
    {
        if(l_set.find(nr_num-1) != l_set.end())
        {
            l_set.erase(nr_num-1);
        }
        else if(l_set.find(nr_num) != l_set.end())
        {
            l_set.erase(nr_num);
        }
        else if(l_set.find(nr_num+1) != l_set.end())
        {
            l_set.erase(nr_num+1);
        }
    }

    answer -= (static_cast<int>(l_set.size()));

    return answer;
   
}

int main()
{
    cout<<solution(5, {4, 2}, {1, 3});
    return 0;
}