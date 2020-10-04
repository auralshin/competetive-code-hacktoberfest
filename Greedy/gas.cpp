#include<bits/stdc++.h>
using namespace std;

int checkGas(vector<int> gas, vector<int> cost, int n)
{
	int t_gas = 0, t_cost = 0;
	t_gas = accumulate(gas.begin(), gas.end(), t_gas);
	t_cost = accumulate(gas.begin(), gas.end(), t_cost);
	cout << t_gas << " " << t_cost;
	 
	if(t_gas < t_cost)
		return -1;
		
	int start = 0;
	int total = 0;
	
	for(int i = 0; i < n; i++)
	{
		total += gas[i] - cost[i];	
		if(total < 0)
		{
			start = i + 1;
			total = 0;
		}
	}
	return start;
	
}


int main()
{
	int n;
	vector<int> gas;
	vector<int> cost;
	
	for(int i = 0;  i < n; i++)
	{
		int temp;
		cin >> temp;
		gas.push_back(temp);
	}
	for(int i = 0;  i < n; i++)
	{
		int temp;
		cin >> temp;
		cost.push_back(temp);
	}
	cout << checkGas(gas, cost, n);
	
}
