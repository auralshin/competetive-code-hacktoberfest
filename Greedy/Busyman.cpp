#include<bits/stdc++.h>
using namespace std;

bool comp(pair<int, int> p1, pair<int, int> p2)
{
	if(p1.second < p2.second)
		return true;
	if(p1.second == p2.second)
	{
		return (p1.first < p2.first);
	}
	return false;
}

int main()
{
	int t;
	cin >> t;
	int m, n;
	vector< pair<int, int> > act;
	while(t--)
	{
		int temp;
		cin >> temp;
		while(temp--)
		{
			
			cin >> m;
			cin >> n;
			act.push_back({m, n});
		}

		sort(act.begin(),act.end(), comp);	
	
		int cnt = 1;
		int start = act[0].second;
	auto it = act;
		for(int i = 1; i < act.size(); i++)
		{
			if(act[i].first >= start)
			{
				start = act[i].second;
				cnt++;
			}
		}
		cout << cnt;
	}		
}
