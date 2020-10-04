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
	
	int profit = 0;
	
	int i = 1;

	while(i < n)
	{
		cout << arr[i] <<endl;
		if(arr[i] > arr[i - 1])
		{
			profit += arr[i] - arr[i - 1];
			cout << profit <<" ";
			i += 2;
		}
		else
			i++;
	}
	cout << profit;
	
}

 
