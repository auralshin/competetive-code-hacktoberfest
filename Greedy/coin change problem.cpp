#include<bits/stdc++.h>
using namespace std;

void coinChange(vector<int> coin, int n)
{
	int ans = 0;
	while(n > 0)
	{
		auto r = upper_bound(coin.begin(), coin.end(), n);
		r--;
		cout << *r << " ";
		n = n - *r;
	}
		
	
}

int main()
{
	vector<int> coin {1, 2, 5, 10, 20, 50, 100, 500};
	int n;
	cin >> n;
	coinChange(coin, n);
	
}
