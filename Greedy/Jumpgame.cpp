#include<bits/stdc++.h>
using namespace std;

int JumpGame(vector<int> arr, int pos)
{
	//backtracking
	if(pos = arr.size() - 1)
		return 1;
	int n = arr.size() - 1;
	int far = min(pos + arr[pos], n);
	for(int i = pos + 1; i <= far; i++)
	{
		if(JumpGame(arr, i))
			return 1;
	}
	return 0;
	
	
//	Greedy
//	int far = 0;
//	for(int i = 0; i <= far && i < n; i++ )
//	{
//		far = max(far, i + arr[i]);
//	}
//	return far >= n - 1;
}


int main()
{
	int n;
	cin >> n;
	vector<int> arr;

	while(n--)
	{
		int temp;
		cin>>temp;
		arr.push_back(temp);
	}
	cout << JumpGame(arr, 0);	

	
}
