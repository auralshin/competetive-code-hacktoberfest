//CPP program to find minimum spanning tree using Kruskal's Algorithm. 
//Here we use Union-Find Algorithm to check whether cycle is formed or not in the graph


// fixed compilation errors | fixed by JosepHyv
// this algorithm is also used to do an MST ( Minimum Spanning Tree )
#include <bits/stdc++.h>

using namespace std;
const int MAX = 1e6 + 7;
int parent[MAX];


int findParent(int x)                                  //helper method to return parent of the particular node
{
    while(parent[x] != x)
    {
        parent[x] = parent[parent[x]];
        x = parent[x];
    }
    return x;
}

void doUnion(int x, int y)                              //helper method to combine nodes which dont form a cycle
{
    int p = findParent(x);
    int q = findParent(y);
    parent[p] = q; // make P parent of q
}

long long kruskal(pair<long long, pair<int, int> > p[], int edges)
{
    int x, y;
    long long cost, minimumCost = 0;
    for(int i = 0;i < edges;++i)
    {
        x = p[i].second.first;                          //Selecting edges one by one in increasing order from the beginning
        y = p[i].second.second;
        cost = p[i].first;
        
        if(findParent(x) != findParent(y))             // check whether selected edge creates a cycle or not
        {
            minimumCost += cost;
            doUnion(x, y);
        }    
    }
    return minimumCost;
}

int main()
{
    
    int x, y,nodes, edges;
    long long weight,minimumCost;
//    pair <long long, pair<int, int> > p[MAX];  MAX is to large for an static local array
    
    for(int i = 0;i < MAX;++i)
        parent[i] = i;

    cin >> nodes >> edges;
    pair <long long, pair<int, int> > p[edges]; // the size  is equal to number of edges

    for(int i = 0;i < edges;++i)
    {
        cin >> x >> y >> weight;
        p[i] = make_pair(weight, make_pair(x, y));   //add the weighted edges to the array containing pair of edges
    }
    sort(p, p + edges);                              // Sort the edges in the ascending order
    minimumCost = kruskal(p, edges); 
    cout << minimumCost << "\n";
    return 0;
}