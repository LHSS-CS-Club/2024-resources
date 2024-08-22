import java.util.ArrayList;
import java.util.PriorityQueue;

// Implementation in Java using priority queue, O(n log n) time (look into priority queue runtime if you are curious)
public class Dijkstras {
    // Simple implementation for edges. Essentially, it takes 3 arguments, a node where it starts, the node it connects
    // to, and the weighting of the edge. Think of it as a line segment, where the origin node is some inital coordinate
    // , the neighbor node is some final coordinate, and the weight is the length of the line segment.
    static class Edge {
        int originNode;
        int neighborNode;
        int weight;

        Edge(int source, int neighbor, int weight) {
            this.originNode = source;
            this.neighborNode = neighbor;
            this.weight = weight;
        }
    }

    // Runs the check for the priority queue. Essentially, for each new element that is added, it checks if its weight
    // is less than the weight of the element before it. Orders nodes based on how low their weightings are.
    static class NodePair implements Comparable<NodePair> {
        int node;
        int currentWeight;

        NodePair(int node, int currentWeight) {
            this.node = node;
            this.currentWeight = currentWeight;
        }

        public int compareTo(NodePair currentNode) {
            return this.currentWeight - currentNode.currentWeight;
        }
    }

    // Driver code
    public static void main(String[] args) {
        // Constructing a graph
        ArrayList<Edge>[] graph = new ArrayList[5];
        for (int i = 0; i < graph.length; i++) {
            graph[i] = new ArrayList<>();
        }

        // Try to add some nodes and edges up here!
        graph[0].add(new Edge(0,1,14));
        graph[0].add(new Edge(0,3,5));

        graph[1].add(new Edge(1,0,14));
        graph[1].add(new Edge(1,4,2));
        graph[1].add(new Edge(1,2,6));

        graph[2].add(new Edge(2,1,6));
        graph[2].add(new Edge(2,4,1));
        graph[2].add(new Edge(2,1,7));

        graph[3].add(new Edge(3,0,5));
        graph[3].add(new Edge(3,4,3));

        graph[4].add(new Edge(4,3,3));
        graph[4].add(new Edge(4,1,2));

        // Starts at the very first node
        int startNode = 0;

        boolean[] visited = new boolean[graph.length];

        // Creating a priority queue
        PriorityQueue<NodePair> pq = new PriorityQueue<>();
        pq.add(new NodePair(startNode, 0));

        // While we still have unexplored nodes
        while (pq.size() > 0) {
            // Our next connected node is going to be the one with the lowest weighting.
            NodePair currentNode = pq.remove();

            // If we have already visited the node, rerun the loop. This node will be removed from the queue.
            if (visited[currentNode.node]) {
                continue;
            }

            // Set the node we just explored to be true, so its not explored again.
            visited[currentNode.node] = true;
            System.out.println("Current Node: " + currentNode.node + ", Distance from starting node: " + currentNode.currentWeight);

            // For each edge that is connected to the current node, go through each one and add it to the priority queue.
            for (Edge edge : graph[currentNode.node]) {
                if (!visited[edge.neighborNode]) {
                    // Add the weightings of all the nodes that were visited.
                    pq.add(new NodePair(edge.neighborNode, currentNode.currentWeight + edge.weight));
                }
            }
        }
    }
}
