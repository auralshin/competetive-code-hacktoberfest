#include<bits/stdc++.h>
using namespace std;

int main()
{
	int n;
	vector<int> arr;
	cin >> n;
	int max = INT_MIN;
	while(n--)
	{
		int t;
		cin >> t;
		arr.push_back(t);
		if(t > max)
			max = t;
	}
	n = arr.size();
	
	vector<int> ans(max + 1, 0);

	for(int i = 0; i < n; i++)
	{
		ans[arr[i]]++;
	}
	int t = 0;
	int min = 0;
	for(int i = 0; i <= max; i++)
	{
		if(ans[i] == 0)
			continue;
		else
		{
			while(ans[i] > 0)
				{
					arr[t] = i;		
//					min += abs(arr[t] - t + 1);	
//					cout << ans[t] << " " << t + 1 << endl;
					 t++;
					ans[i]--;
				}
			}	
	}
	for(int i = 0; i < n; i++)
	{
//		cout << arr[i] <<" "<< i + 1<< endl;
		min += abs(arr[i] - (i + 1));
 	}
	
	cout << "\n" << min;	
}
