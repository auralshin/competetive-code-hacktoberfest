/**
**How Kruskal's algorithm works**

It falls under a class of algorithms called greedy algorithms that find the local optimum in the hopes of finding a global optimum.  

We start from the edges with the lowest weight and keep adding edges until we reach our goal.  

The steps for implementing Kruskal's algorithm are as follows:  

* Sort all the edges from low weight to high.  
* Take the edge with the lowest weight and add it to the spanning tree. If adding the edge created a cycle, then reject this edge.  
* Keep adding edges until we reach all vertices.  

References : https://www.programiz.com/dsa/kruskal-algorithm
             https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
*/
import java.util.*; 
import java.lang.*; 
import java.io.*; 
  
public class Kruskal { 
    static class Edge implements Comparable<Edge> { 
        int src, dest, weight; 
  
        @Override
        public int compareTo(Edge compareEdge) { 
            return this.weight - compareEdge.weight; 
        } 
    }; 
  
    static class Subset  { 
        int parent, rank; 
    }; 
  
    
  
    static class Graph {
        private Integer V;
        private Integer E;
        private final List<Edge> edges; 
        public Graph(int vertices, int edge)  { 
            V = vertices; 
            E = edge; 
            edges = new ArrayList<>(); 
            for (int i = 0; i < E; ++i) 
                edges.add(new Edge()); 
        }

        public void addEdge(int index, int source, int destination, int weight) {
            edges.get(index).src = source;
            edges.get(index).dest = destination;
            edges.get(index).weight = weight;
        }
        public List<Edge> getEdges() {
            return edges;
        }
        public int getVertices() {
            return V;
        }

        public int getEdge() {
            return E;
        }
    }
  
    // A utility function to find set of an element i 
    // (uses path compression technique) 
    public static int find(Subset subsets[], int i)  { 
        // find root and make root as parent of i (path compression) 
        if (subsets[i].parent != i) 
            subsets[i].parent = find(subsets, subsets[i].parent); 
  
        return subsets[i].parent; 
    } 
  
    // A function that does union of two sets of x and y 
    // (uses union by rank) 
    public static void union(Subset subsets[], int x, int y) { 
        int xroot = find(subsets, x); 
        int yroot = find(subsets, y); 
  
        // Attach smaller rank tree under root of high rank tree 
        // (Union by Rank) 
        if (subsets[xroot].rank < subsets[yroot].rank) 
            subsets[xroot].parent = yroot; 
        else if (subsets[xroot].rank > subsets[yroot].rank) 
            subsets[yroot].parent = xroot; 
  
        // If ranks are same, then make one as root and increment 
        // its rank by one 
        else { 
            subsets[yroot].parent = xroot; 
            subsets[xroot].rank++; 
        } 
    } 
  
    // The main function to construct MST using Kruskal's algorithm 
    public static void kruskalAlgorithm(Graph graph) { 
        int V = graph.getVertices();
        Edge result[] = new Edge[V];  // This will store the resultant MST 
        int e = 0;  // An index variable, used for result[] 
        int i = 0;  // An index variable, used for sorted edges 
        for (i=0; i<V; ++i) 
            result[i] = new Edge(); 
  
        // Step 1:  Sort all the edges in non-decreasing order of their 
        // weight.  If we are not allowed to change the given graph, we 
        // can create a copy of array of edges
        List<Edge> edge = graph.getEdges(); 
        Collections.sort(edge); 
  
        // Allocate memory for creating V ssubsets 
        Subset subsets[] = new Subset[V]; 
        for(i=0; i<V; ++i) 
            subsets[i]=new Subset(); 
  
        // Create V subsets with single elements 
        for (int v = 0; v < V; ++v) { 
            subsets[v].parent = v; 
            subsets[v].rank = 0; 
        } 
  
        i = 0;  // Index used to pick next edge 
  
        // Number of edges to be taken is equal to V-1 
        while (e < V - 1)  { 
            // Step 2: Pick the smallest edge. And increment  
            // the index for next iteration 
            Edge next_edge = new Edge(); 
            next_edge = edge.get(i++);
  
            int x = find(subsets, next_edge.src); 
            int y = find(subsets, next_edge.dest); 
  
            // If including this edge does't cause cycle, 
            // include it in result and increment the index  
            // of result for next edge 
            if (x != y)  { 
                result[e++] = next_edge; 
                union(subsets, x, y); 
            } 
            // Else discard the next_edge 
        } 
  
        // print the contents of result[] to display 
        // the built MST 
        System.out.println("Following are the edges in " +  
                                     "the constructed MST"); 
        for (i = 0; i < e; ++i) 
            System.out.println(result[i].src+" -- " +  
                   result[i].dest+" == " + result[i].weight); 
    } 
  
    // Driver Program 
    public static void main (String... args) { 
  
        /* Let us create following weighted graph 
                 10 
            0--------1 
            |  \     | 
           6|   5\   |15 
            |      \ | 
            2--------3 
                4       */
        int V = 4;  // Number of vertices in graph 
        int E = 5;  // Number of edges in graph 
        Graph graph = new Graph(V, E); 
  
        // add edge 0-1 
        graph.addEdge(0, 0, 1, 10);
  
        // add edge 0-2 
        graph.addEdge(1, 0, 2, 6);
  
        // add edge 0-3 
        graph.addEdge(2, 0, 3, 5);
  
        // add edge 1-3 
        graph.addEdge(3, 1, 3, 15);
  
        // add edge 2-3 
        graph.addEdge(4, 2, 3, 4);
  
        kruskalAlgorithm(graph); 
    } 
} 