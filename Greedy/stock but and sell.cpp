#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	vector<int> arr;
	cin >> n;
	while(n--)
	{
		int t;
		cin >> t;
		arr.push_back(t);
	}
	n = arr.size();
//	int profit = 0;
	int i, j, flag = 0;

//6	
//6 1 3 2 4 7
	int profit = INT_MIN;
	int maxi = arr[n - 1];
	
	for(int i = n - 2; i >= 0; i--)
	{
		if(maxi < arr[i])
		{
			maxi = arr[i];
		}
		else
		{
			int t = maxi - arr[i];
			profit = max(profit, t);
		}		
	}
	cout << profit;
	
}
