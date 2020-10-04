#include<bits/stdc++.h>
using namespace std;

void solve()
{
	int n;
	cin >> n;
	vector<int> arr(n);
	
	for(int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	
	int low = 0;
	int high = n-1;
	
	while(low <= high){
		
		int mid = (low + high)/2;
		
		if(arr[mid] <= arr[mid-1] && arr[mid] <= arr[mid+1])		
		{
			cout<<mid+1;
			break;
		}
		else if( arr[mid] < arr[high] )
		{
			high = mid-1;
		}
		else
		{
			low = mid+1;
		}
	}

}

int main()
{
    ios_base::sync_with_stdio(false);
    
 	cin.tie(NULL);
 	cout.tie(NULL);

	int t;
	cin >> t;
	
	while(t--)
	{
		solve();
	} 	
}
