#include<bits/stdc++.h>
using namespace std;

const int N = 1e5+10;
vector<int> g[N]; // Graph representing adjacency list 
bool canBeVisited[N]; // Boolean array for keeping the track of all visited vertices

void DFS(int vertex) {
    canBeVisited[vertex] = true; // Current vertex is marked as visited
    for (int child : g[vertex]) { // Traversing the all adjacent vertices of the current vertex
        if (canBeVisited[child] == false) { // If an adjacent vertex is found to be not visited yet, DFS is called
            DFS(child);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);  cout.tie(0);

    int n,e;  cin>>n>>e; // Input system: the number of vertices (n) and edges (e)

    // Taking input of the edges and then constructing the graph using the already created adjacency list
    for (int i=0; i<e; i++) {
        int v1,v2;
        cin>>v1>>v2;

        g[v1].push_back(v2); // connecting the v1 edge with v2 edge
        g[v2].push_back(v1); // Adding the edge (v2, v1) since the graph is undirected
    }

    int connectedComponentCounter = 0; // Counter to count the number of connected components in the graph

    // Executing DFS on all vertices to find connected components
    // If the vertex is not visited yet, DFS starts to execute from that vertex
    for (int i=0; i<n; i++) {
        if (canBeVisited[i] == false) { // Starting DFS from that vertex which is not visited yet
            DFS(i);
            connectedComponentCounter++; // Incremening the counter if any disconnected component is found
        }
    }

    //Result output
    if (connectedComponentCounter > 1)
        cout<<"false\n"; // If the number of connected component exceeds 1, the isn't connected so there is no valid path
    else
        cout<<"true\n"; // If there is only one connected component, the graph is connected

    return 0;
}
