#include<bits/stdc++.h>
using namespace std;

void solve()
{
	int n;
	cin >> n;

	int k;
	cin >> k;

	vector<int> arr(n);

	int first = 0, last = 0;

	for(int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}

	int low = 0, high = n-1;
	
	while(low<=high)
	{
		int mid = high + (low-high)/2;

		if(arr[mid] == k){
			first = mid;
			high = mid-1;
		}

		if(arr[mid] > k){
			high = mid - 1;
		}
		else if(arr[mid] < k){
			low = mid + 1;
		}
	}	

	low = 0;
	high = n-1;
	
	while(low<=high)
	{
		int mid = high + (low-high)/2;
		
		if(arr[mid] == k){
			last = mid;
			low = mid+1;
		}

		if(arr[mid] > k){
			high = mid - 1;
		}
		else{
			low = mid + 1;
		}
	}
	cout<<first << " " << last;	
}

int main()
{
    ios_base::sync_with_stdio(false);
    
 	cin.tie(NULL);
 	cout.tie(NULL);

		solve();
	
}
