import heapq

def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity except for the start node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Use a priority queue (heap) to track nodes with the shortest distance
    pq = [(0, start)]  # (distance, node)
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Ignore outdated nodes
        if current_distance > distances[current_node]:
            continue
        
        # Check neighbors and update distances
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example graph represented as an adjacency list
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'A': 2, 'C': 1, 'D': 7},
    'C': {'A': 5, 'B': 1, 'D': 3},
    'D': {'B': 7, 'C': 3}
}

start_node = 'A'
shortest_distances = dijkstra(graph, start_node)

print("Shortest distances from node", start_node + ":")
for node, distance in shortest_distances.items():
    print(f"To node {node}: {distance}")
