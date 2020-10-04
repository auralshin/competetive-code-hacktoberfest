#include<bits/stdc++.h>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    
 	cin.tie(NULL);
 	cout.tie(NULL);
 	
	int n = 6;
	vector<int> arr {4, 5, 6 ,7, 2, 3};

	int low = 0;
	int high = n-1;
	
	 if(n == 1)
	 cout << arr[0];
//        return arr[0];
    if(arr[high] > arr[0])
            cout << arr[0];
	
	
	while(low < high){
		int mid = low + (high-low)/2;

		if(arr[mid] > arr[mid + 1])
		{
			cout << arr[mid];
			break;
		}
		
		if(arr[mid-1] > arr[mid])
		{
			cout << arr[mid];
			break; 
		}
		
		if(arr[mid] > arr[low]){
			low = mid+1;
		}
		else{
			high = mid - 1;
		}
	}
			
}
