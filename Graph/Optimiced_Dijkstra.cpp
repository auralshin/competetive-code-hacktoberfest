// contribution of Joseph Hynimoto Aguilar Lopez | JosepHyv
#include <queue>
#include <vector>
#include <iostream>
using namespace std;


/* 
dijkstra can be implemented using a 
priority_queue and the complexity is 
O( V + E log V ) better than of O(V^2)

however if the problem requires calculate 
the distance of all Vertices, dijkstra will be 
inefficient :(  and other algorithms will be better*/ 

/// this struct is for graph
struct vertice
{
	int v;
	int weight;
};

/// this struct is only for dijkstra
struct node
{
	int v;
	long long int total; /// this data type is for  big weights 
	bool operator < ( const node &o) const
	{
		return total < o.total;
	}
	/*we overload the < operator 
	 the priority_queue need be a min heap
	 if the problem requieres a max heap, this overload
	 will be uncessary */
};

							/// this vector can be a matrix[V][V]
							/// or vector < vertice > graph[V];
void dijkstra(int start, int end, vector < vector < vertice > > graph)
{
	priority_queue< node > dijks;
	vector < bool > vis( (int) graph.size() );
	vis[start] = true;

	/// this algorithm is very similar to classic BFS algorithm
	dijks.push({start,0});
	while( dijks.size() )
	{
		node root = dijks.top();
		dijks.pop();

		cerr<<" -> "<<root.v<<" "<<root.total<<"\n";
		if( root.v == end)
		{
			cout<<"minimal distance of " << start << " to "<<end<<"\n";
			cout<<root.total<<"\n";
			return;
		}
		
		for( vertice curr : graph[root.v] ) 
		{
			node son  = root;
			if( !vis[curr.v])
			{
				son.total += curr.weight;
				son.v = curr.v;
				vis[curr.v] = true;
				dijks.push(son);
			}
		}

	}

	cout<<"Can't found a minimal path\n";
	return;
}


int main()
{
	int V; // num of vertices
	int E; // num of edjes;
	cin>>V>>E;
	vector < vector < vertice > > graph(V+1); // reseve memory
	/// this case will be an undirected graph

	for(int c = 0 ; c<V; c++)
	{
		/// A to B with weight X
		int A,B,X;
		cin>>A>>B>>X;
		graph[A].push_back({B,X});
		/// other form of make push in pair struct 
		/// graph[A].push_back( {.v = B, .weight = X});
		graph[B].push_back({A,X});
	}

	/// shortes path from 1 to 5
	dijkstra(1,5,graph);
}	

/// test case
/*

5 6
1 2 2
2 5 5
2 3 4
1 4 1
4 3 3
3 5 1

*/ 


/// other ways for implement a graph are
/// using std::vector and std::pair
/* 
	Static: vector < pair < DATA, DATA > > graph[Vertices];
	Dinamic vector < vector < pair < DATA, DATA > > > graph(Vertices);
	Dinamic with initialized edges vector < vector < pair < DATA, DATA > > > graph( Vertices, , vector < pair < DATA, DATA > > (E, {data, data}) );
*/

/// Using Matrix 
/*
	Data Graph[V][V]; memory O( v^2);
*/


