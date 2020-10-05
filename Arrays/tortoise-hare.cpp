// CPP program to find a duplicate 
// element in an array with values in 
// range from 0 to n-1. 


#include <bits/stdc++.h> 
using namespace std; 

// function to find one duplicate 
int findduplicate(const int arr[], int n) 
{ 
	// return -1 because in these cases 
	// there can not be any repeated element 
	if (n <= 1) 
		return -1; 

	// initialize fast and slow 
	int slow = arr[0]; 
	int fast = arr[arr[0]]; 

	// loop to enter in the cycle 
	while (fast != slow) { 

		// move one step for slow 
		slow = arr[slow]; 

		// move two step for fast 
		fast = arr[arr[fast]]; 
	} 

	// loop to find entry point of the cycle 
	fast = 0; 
	while (slow != fast) { 
		slow = arr[slow]; 
		fast = arr[fast]; 
	} 
	return slow; 
} 

int main() 
{ 
	const int arr[] = { 1, 2, 3, 4, 5, 6, 3 }; 
	int n = sizeof(arr) / sizeof(arr[0]); 
	cout << findduplicate(arr, n); 
	return 0; 
} 
