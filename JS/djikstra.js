//Js program to implement djikstra algorithm  using adjacency list representation.
class Graph {
    constructor() {
      this.nodes = [];                                       
      this.adjacencyList = {};
    }
    addNode(node) {                                         //helper method to add nodes to the node array of a graph
        this.nodes.push(node); 
        this.adjacencyList[node] = [];
    }
    addEdge(node1, node2, weight) {                         //helper method to add edges to the graph(Note :The graph considered herecontains undirected edges)
        this.adjacencyList[node1].push({node:node2, weight: weight});
        this.adjacencyList[node2].push({node:node1, weight: weight});
    }
}

class PriorityQueue {
    constructor() {
      this.collection = [];                                   //initialize an empty araay
    }
    enqueue(element){                                         //helper method to add elements to queue
        if (this.isEmpty()){ 
          this.collection.push(element);                      // add the array elements to the collection
        } else {
          let added = false;                                  // here nodes will be placed in ascending order of their distance
          for (let i = 1; i <= this.collection.length; i++){  //insert the node before the first element we find that has a larger weight than our node.
            if (element[1] < this.collection[i-1][1]){ 
              this.collection.splice(i-1, 0, element);
              added = true;
              break;
            }
          }
          if (!added){
              this.collection.push(element);
          }
        }
      };
      dequeue() {                                             //helper method to take out top element at the queue
        let value = this.collection.shift();
        return value;
      };
}

function findPathWithDijkstra(startNode, endNode) {
    let distance = {};                                         //initialize distance object for storing distances of various nodes from starting node
    let backtrace = {};
    let pq = new PriorityQueue();                              //create a priority queue object

    distance[startNode] = 0;                                  //make distance for start node as 0
  
    this.nodes.forEach(node => {
      if (node !== startNode) {
        distance[node] = Infinity;                           //initialize distance for rest nodes as infinity
      }
    });
    pq.enqueue([startNode, 0]);                              //add first node to the priority queue

    while (!pq.isEmpty()) {
        let shortestStep = pq.dequeue();                     //take out first node from the priority queue
        let currentNode = shortestStep[0];                   //node is first element of the array
        this.adjacencyList[currentNode].forEach(neighbor => {
        

          if (distance[currentNode] + neighbor.weight < distance[neighbor.node]) {   // update the distance for neighbour node if its already provided distance is more than distance of current node added to weight of neighbour node
            distance[neighbor.node] = times[currentNode] + neighbor.weight;
            backtrace[neighbor.node] = currentNode;                                  // add the backtraced node for the neighbour node
            pq.enqueue([neighbor.node, distance[currentNode] + neighbor.weight]);    // add the neighbour node with its updated distance to priority queue
          }
        });
      }

      let path = [endNode];
      let lastStep = endNode;
      while(lastStep !== startNode) {
        path.unshift(backtrace[lastStep]);                                           // move the backtraced node for the last step taken to front of the path array
        lastStep = backtrace[lastStep];
      }
      return `Shortest Distance between ${startNode} and ${endNode} is ${distance[endNode]}`;
    }




