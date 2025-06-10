"""
Dijkstra's Shortest Path Algorithm Implementation
"""

import heapq


def dijkstra(graph, start):
    """
    Dijkstra's algorithm for finding shortest paths from a single source.
    
    Time Complexity: O((V + E) log V) with binary heap
    Space Complexity: O(V)
    
    Args:
        graph: Graph object
        start: Starting vertex
        
    Returns:
        distances: Dictionary mapping each vertex to its shortest distance from start
        predecessors: Dictionary mapping each vertex to its predecessor in the shortest path
    """
    # Initialize distances to infinity and predecessors to None
    distances = {vertex: float('inf') for vertex in graph.vertices}
    predecessors = {vertex: None for vertex in graph.vertices}
    
    # Distance to start vertex is 0
    distances[start] = 0
    
    # Priority queue stores tuples of (distance, vertex)
    # Python's heapq implements a min-heap
    priority_queue = [(0, start)]
    
    # Set to track visited vertices
    visited = set()
    
    while priority_queue:
        # Extract vertex with minimum distance
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Skip if already processed
        if current_vertex in visited:
            continue
        
        # Mark as visited
        visited.add(current_vertex)
        
        # If we extracted a vertex with infinite distance, remaining vertices are unreachable
        if current_distance == float('inf'):
            break
        
        # Examine all neighbors of current vertex
        for neighbor, edge_weight in graph.get_neighbors(current_vertex):
            # Skip if already visited
            if neighbor in visited:
                continue
            
            # Calculate new distance through current vertex
            new_distance = current_distance + edge_weight
            
            # If we found a shorter path, update it
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_vertex
                
                # Add to priority queue for future processing
                heapq.heappush(priority_queue, (new_distance, neighbor))
    
    return distances, predecessors


def dijkstra_path(graph, start, end):
    """
    Find the shortest path between two vertices using Dijkstra's algorithm.
    
    Args:
        graph: Graph object
        start: Starting vertex
        end: Ending vertex
        
    Returns:
        Tuple of (path, distance) where:
        - path is a list of vertices from start to end
        - distance is the total distance
        Returns (None, float('inf')) if no path exists
    """
    distances, predecessors = dijkstra(graph, start)
    
    # Check if end is reachable
    if distances[end] == float('inf'):
        return None, float('inf')
    
    # Reconstruct path
    path = graph.reconstruct_path(predecessors, start, end)
    
    return path, distances[end]


def validate_graph_for_dijkstra(graph):
    """
    Validate that the graph is suitable for Dijkstra's algorithm.
    
    Args:
        graph: Graph object
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    # Check for negative edges
    for u in graph.vertices:
        for v, weight in graph.get_neighbors(u):
            if weight < 0:
                return False, f"Negative edge found: {u} -> {v} with weight {weight}"
    
    return True, None