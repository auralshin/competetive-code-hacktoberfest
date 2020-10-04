#include<bits/stdc++.h>
#include<iostream>
using namespace std;
 
#define ff              first
#define ss              second
#define ll              long long int
#define mod             1000000007
#define inf             1e18
#define loop(i,a,b)     for(int i=(a);i<=(b);i++)
#define loopd(i,a,b)    for(int i=(a);i>=(b);i--)
#define w(x)            int x; cin>>x; while(x--)
mt19937                 rng(chrono::steady_clock::now().time_since_epoch().count());
 void rotatea(int a[][100],int n)
 { 

   for(int i=0;i<n;i++)  //reverse all rows
   {
     
       reverse(a[i],a[i]+n);
  }

  for(int i=0;i<n;i++)
  {
    for(int j=0;j<n;j++)
    {
      if(i>j)
       swap(a[i][j],a[j][i]);
    }
  }
   






 }
int32_t main()
{
ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
 
 int a[100][100]={0};
 int n;
 cin>>n;
 for(int i=0;i<n;i++)
 {
   for(int j=0;j<n;j++)
   {
     cin>>a[i][j];
   }
 }
 
 rotatea(a,n);

  for(int i=0;i<n;i++)
 {
   for(int j=0;j<n;j++)
   {
     cout<<a[i][j]<<" ";
   }
   cout<<endl;
 }
 
return 0;
    
    
}