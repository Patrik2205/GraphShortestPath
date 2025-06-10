#!/usr/bin/env python3
"""
Example usage of Dijkstra's algorithm implementation
"""

from src.graph import Graph
from src.dijkstra import dijkstra, dijkstra_path, validate_graph_for_dijkstra
from src.visualization import visualize_graph, visualize_path, visualize_dijkstra_progress


def example_image_graph():
    """Example using the graph from the provided image"""
    print("=" * 60)
    print("Example 1: Graph from Image")
    print("=" * 60)
    
    # Create the graph from the image
    graph = Graph(directed=False)
    graph.add_edge('1', '2', 2)
    graph.add_edge('1', '3', 10)
    graph.add_edge('1', '4', 8)
    graph.add_edge('2', '5', 4)
    graph.add_edge('3', '4', 3)
    graph.add_edge('4', '5', 1)
    
    # Validate graph
    is_valid, error_msg = validate_graph_for_dijkstra(graph)
    if not is_valid:
        print(f"Error: {error_msg}")
        return
    
    # Visualize the original graph
    print("\nVisualizing the graph...")
    visualize_graph(graph, title="Example Graph from Image")
    
    # Run Dijkstra from vertex 1
    start_vertex = '1'
    print(f"\nRunning Dijkstra's algorithm from vertex '{start_vertex}'...")
    distances, predecessors = dijkstra(graph, start_vertex)
    
    # Display results
    print(f"\nShortest distances from vertex '{start_vertex}':")
    print("-" * 30)
    for vertex in sorted(graph.vertices):
        if distances[vertex] == float('inf'):
            print(f"{start_vertex} -> {vertex}: No path")
        else:
            print(f"{start_vertex} -> {vertex}: {distances[vertex]}")
    
    # Find specific paths
    print("\nSpecific paths:")
    for end_vertex in ['3', '5']:
        path, distance = dijkstra_path(graph, start_vertex, end_vertex)
        if path:
            print(f"Path from {start_vertex} to {end_vertex}: {' -> '.join(path)} (distance: {distance})")
    
    # Visualize shortest path tree
    visualize_dijkstra_progress(graph, start_vertex, distances, predecessors,
                               title=f"Dijkstra's Result from vertex '{start_vertex}'")
    
    # Visualize specific path
    path, _ = dijkstra_path(graph, '1', '5')
    visualize_path(graph, path, title="Shortest Path: 1 to 5")


def example_directed_graph():
    """Example with directed graph"""
    print("\n" + "=" * 60)
    print("Example 2: Directed Graph")
    print("=" * 60)
    
    # Create a directed graph
    graph = Graph(directed=True)
    edges = [
        ('S', 'A', 7), ('S', 'B', 5),
        ('A', 'B', 3), ('A', 'C', 9), ('A', 'D', 12),
        ('B', 'C', 6), ('B', 'D', 4),
        ('C', 'D', 2), ('C', 'E', 7),
        ('D', 'E', 5)
    ]
    
    for u, v, w in edges:
        graph.add_edge(u, v, w)
    
    # Run Dijkstra from S
    start = 'S'
    distances, predecessors = dijkstra(graph, start)
    
    print(f"\nShortest distances from '{start}':")
    for vertex in sorted(graph.vertices):
        if distances[vertex] == float('inf'):
            print(f"{start} -> {vertex}: No path")
        else:
            path = graph.reconstruct_path(predecessors, start, vertex)
            print(f"{start} -> {vertex}: {distances[vertex]} (path: {' -> '.join(path)})")
    
    # Visualize
    visualize_dijkstra_progress(graph, start, distances, predecessors,
                               title="Directed Graph - Dijkstra from S")


def example_step_by_step():
    """Show Dijkstra's algorithm step by step"""
    print("\n" + "=" * 60)
    print("Example 3: Step-by-Step Execution")
    print("=" * 60)
    
    # Small graph for demonstration
    graph = Graph(directed=False)
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 8)
    graph.add_edge('C', 'E', 10)
    graph.add_edge('D', 'E', 2)
    
    start = 'A'
    print(f"\nExecuting Dijkstra's algorithm from '{start}':")
    print("\nStep-by-step process:")
    print("1. Initialize: All distances = ∞, distance[A] = 0")
    print("2. Priority queue: [(0, A)]")
    print("3. Process vertices in order of increasing distance...")
    
    distances, predecessors = dijkstra(graph, start)
    
    print("\nFinal shortest path tree:")
    for vertex in sorted(graph.vertices):
        if vertex != start and predecessors[vertex]:
            print(f"  {predecessors[vertex]} -> {vertex} (weight: {distances[vertex] - distances[predecessors[vertex]]})")


def example_performance():
    """Example showing performance characteristics"""
    print("\n" + "=" * 60)
    print("Example 4: Performance Analysis")
    print("=" * 60)
    
    import time
    
    # Create graphs of different sizes
    sizes = [10, 20, 50]
    
    for n in sizes:
        # Create a complete graph
        graph = Graph(directed=False)
        
        # Add vertices and edges
        vertices = [f"V{i}" for i in range(n)]
        edge_count = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                # Random-like weights based on indices
                weight = ((i + j) * 7) % 20 + 1
                graph.add_edge(vertices[i], vertices[j], weight)
                edge_count += 1
        
        # Measure time
        start_time = time.time()
        distances, _ = dijkstra(graph, vertices[0])
        end_time = time.time()
        
        print(f"\nGraph size: {n} vertices, {edge_count} edges")
        print(f"Execution time: {(end_time - start_time) * 1000:.2f} ms")
        print(f"Time per vertex: {(end_time - start_time) * 1000 / n:.3f} ms")


if __name__ == "__main__":
    # Run all examples
    example_image_graph()
    example_directed_graph()
    example_step_by_step()
    example_performance()
    
    print("\n" + "=" * 60)
    print("All examples completed!")
    print("\nTo use with your own data:")
    print("  python main.py your_graph.txt -s start_vertex -v")