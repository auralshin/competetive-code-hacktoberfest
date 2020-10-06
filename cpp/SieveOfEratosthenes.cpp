#include <iostream>
using namespace std;

// Primality check of an non-negative Integer 'n' where n<10^6

#define maxN 1000001
bool prime[maxN];

void sieve() {
    for(int i=0; i<maxN; i++)
        prime[i]=true;
    
    prime[0]=prime[1]=false;
    for(int i=2; i*i<maxN; i++) {
        if(prime[i]) {
            for(int j=i*i; j<maxN; j+=i)
                prime[j]=false;
        }
    }
}

int main() {
    sieve();
    int n;
    cin>>n;
    if(n>1000000) {
        cout<<"Invalid Range\n";
        return -1;
    }
    else {
        if(prime[n])
            cout<<"Given number is a prime\n";
        else
            cout<<"Given number is not a prime\n";
    }
    return 0;
}