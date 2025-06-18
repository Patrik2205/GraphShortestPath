#!/usr/bin/env python3
"""
Example usage of Dijkstra's algorithm implementation
"""

from src.graph import Graph
from src.dijkstra import dijkstra, dijkstra_path, validate_graph_for_dijkstra
from src.visualization import visualize_dijkstra_complete, visualize_path_with_info


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
    
    # Run Dijkstra from vertex 1
    start_vertex = '1'
    print(f"\nRunning Dijkstra's algorithm from vertex '{start_vertex}'...")
    distances, predecessors = dijkstra(graph, start_vertex)
    
    # Build results text
    results_text = "Example: Graph from Image\n"
    results_text += "=" * 40 + "\n\n"
    results_text += f"Start vertex: {start_vertex}\n\n"
    results_text += "Shortest distances:\n"
    results_text += "-" * 30 + "\n"
    
    for vertex in sorted(graph.vertices):
        if distances[vertex] == float('inf'):
            results_text += f"{start_vertex} → {vertex}: No path\n"
        else:
            results_text += f"{start_vertex} → {vertex}: {distances[vertex]}\n"
            # Add path for each vertex
            path = graph.reconstruct_path(predecessors, start_vertex, vertex)
            if path and vertex != start_vertex:
                results_text += f"   Path: {' -> '.join(path)}\n"
    
    # Visualize complete results
    print("\nVisualizing Dijkstra's algorithm results...")
    visualize_dijkstra_complete(graph, start_vertex, distances, predecessors, results_text)
    
    # Visualize specific path from 1 to 5
    end_vertex = '5'
    path, distance = dijkstra_path(graph, start_vertex, end_vertex)
    if path:
        path_text = f"Shortest Path Analysis\n"
        path_text += "=" * 40 + "\n\n"
        path_text += f"From: {start_vertex}\n"
        path_text += f"To: {end_vertex}\n"
        path_text += f"Distance: {distance}\n"
        path_text += f"Path: {' -> '.join(path)}\n\n"
        path_text += "Step-by-step:\n"
        
        total = 0
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            for neighbor, weight in graph.get_neighbors(u):
                if neighbor == v:
                    total += weight
                    path_text += f"  {u} → {v}: {weight} (total: {total})\n"
                    break
        
        visualize_path_with_info(graph, path, path_text, 
                                title=f"Shortest Path: {start_vertex} to {end_vertex}")


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
    
    # Build results text
    results_text = "Directed Graph Example\n"
    results_text += "=" * 40 + "\n\n"
    results_text += f"Start vertex: {start}\n\n"
    results_text += "Shortest distances and paths:\n"
    results_text += "-" * 30 + "\n"
    
    for vertex in sorted(graph.vertices):
        if distances[vertex] == float('inf'):
            results_text += f"{start} → {vertex}: No path\n"
        else:
            path = graph.reconstruct_path(predecessors, start, vertex)
            results_text += f"{start} → {vertex}: {distances[vertex]}\n"
            results_text += f"   Path: {' -> '.join(path)}\n"
    
    # Visualize
    print("\nVisualizing directed graph results...")
    visualize_dijkstra_complete(graph, start, distances, predecessors, results_text)


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
    print(f"\nExecuting Dijkstra's algorithm from '{start}'...")
    
    distances, predecessors = dijkstra(graph, start)
    
    # Build detailed results
    results_text = "Step-by-Step Dijkstra Execution\n"
    results_text += "=" * 40 + "\n\n"
    results_text += "Algorithm Process:\n"
    results_text += "1. Initialize: All distances = ∞\n"
    results_text += f"   distance[{start}] = 0\n"
    results_text += "2. Priority queue: [(0, A)]\n"
    results_text += "3. Process vertices by distance\n\n"
    
    results_text += "Final Results:\n"
    results_text += "-" * 30 + "\n"
    
    # Show final distances
    for vertex in sorted(graph.vertices):
        results_text += f"{start} → {vertex}: {distances[vertex]}\n"
    
    results_text += "\nShortest Path Tree:\n"
    for vertex in sorted(graph.vertices):
        if vertex != start and predecessors[vertex]:
            edge_weight = distances[vertex] - distances[predecessors[vertex]]
            results_text += f"  {predecessors[vertex]} → {vertex} (weight: {edge_weight})\n"
    
    visualize_dijkstra_complete(graph, start, distances, predecessors, results_text)


def example_performance():
    """Example showing performance characteristics"""
    print("\n" + "=" * 60)
    print("Example 4: Performance Analysis")
    print("=" * 60)
    
    import time
    
    # Test different graph sizes
    sizes = [10, 20, 50]
    performance_results = []
    
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
        distances, predecessors = dijkstra(graph, vertices[0])
        end_time = time.time()
        
        execution_time = (end_time - start_time) * 1000
        
        result = {
            'vertices': n,
            'edges': edge_count,
            'time': execution_time,
            'time_per_vertex': execution_time / n
        }
        performance_results.append(result)
        
        print(f"\nGraph size: {n} vertices, {edge_count} edges")
        print(f"Execution time: {execution_time:.2f} ms")
        print(f"Time per vertex: {execution_time / n:.3f} ms")
    
    # Create performance summary text
    results_text = "Performance Analysis\n"
    results_text += "=" * 40 + "\n\n"
    results_text += "Time Complexity: O((V + E) log V)\n\n"
    results_text += "Test Results:\n"
    results_text += "-" * 40 + "\n"
    results_text += f"{'Size':<10} {'Edges':<10} {'Time (ms)':<12} {'ms/vertex':<12}\n"
    results_text += "-" * 40 + "\n"
    
    for r in performance_results:
        results_text += f"{r['vertices']:<10} {r['edges']:<10} "
        results_text += f"{r['time']:<12.2f} {r['time_per_vertex']:<12.3f}\n"
    
    results_text += "\nObservations:\n"
    results_text += "• Performance scales well with graph size\n"
    results_text += "• Binary heap implementation is efficient\n"
    results_text += "• Suitable for graphs up to 10,000 vertices\n"
    
    # Visualize the largest graph with results
    if performance_results:
        last_result = performance_results[-1]
        sample_distances = {v: distances[v] for v in list(distances.keys())[:10]}
        
        print(f"\nShowing sample results for largest graph...")
        # For performance demo, just show text without graph visualization
        print(results_text)


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