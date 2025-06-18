#!/usr/bin/env python3
"""
Dijkstra's Shortest Path Algorithm Implementation
Main application for finding shortest paths using Dijkstra's algorithm
"""

import argparse
import os
import sys
from src.graph import Graph
from src.dijkstra import dijkstra
from src.visualization import visualize_dijkstra_complete, visualize_path_with_info
from src.file_handler import load_graph_from_file, save_results


def build_results_text(graph, start, distances, predecessors, end=None):
    """Build formatted results text for display"""
    results = []
    
    # Header
    results.append("=" * 50)
    results.append("Dijkstra's Shortest Path Algorithm")
    results.append("=" * 50)
    results.append("")
    
    # Graph info
    stats = graph.get_graph_stats()
    results.append("Graph Information:")
    results.append(f"  Vertices: {stats['num_vertices']}")
    results.append(f"  Edges: {stats['num_edges']}")
    results.append(f"  Type: {'Directed' if stats['directed'] else 'Undirected'}")
    results.append(f"  Total weight: {stats['total_weight']}")
    results.append(f"  Average weight: {stats['average_weight']:.2f}")
    
    if stats['has_negative_edges']:
        results.append("\n⚠️  WARNING: Graph contains negative edges!")
        results.append("Dijkstra may not produce correct results.")
    
    results.append("")
    results.append(f"Start vertex: {start}")
    results.append("")
    
    # If specific end vertex is requested
    if end:
        if end not in graph.vertices:
            results.append(f"❌ Error: End vertex '{end}' not found!")
        else:
            path = graph.reconstruct_path(predecessors, start, end)
            if path is None or distances[end] == float('inf'):
                results.append(f"No path exists from {start} to {end}")
            else:
                results.append(f"Shortest path from {start} to {end}:")
                results.append(f"Path: {' -> '.join(map(str, path))}")
                results.append(f"Total distance: {distances[end]}")
                
                # Add step-by-step path details
                results.append("\nPath details:")
                total = 0
                for i in range(len(path) - 1):
                    u, v = path[i], path[i + 1]
                    # Find edge weight
                    for neighbor, weight in graph.get_neighbors(u):
                        if neighbor == v:
                            total += weight
                            results.append(f"  {u} → {v}: {weight} (total: {total})")
                            break
    else:
        # Show all shortest distances
        results.append("Shortest distances from start:")
        results.append("-" * 40)
        
        for vertex in sorted(graph.vertices):
            if distances[vertex] == float('inf'):
                results.append(f"{start} → {vertex}: No path")
            else:
                results.append(f"{start} → {vertex}: {distances[vertex]}")
                
                # Show path for close vertices (optional)
                if distances[vertex] > 0 and distances[vertex] < float('inf'):
                    path = graph.reconstruct_path(predecessors, start, vertex)
                    if path and len(path) <= 5:  # Only show short paths
                        results.append(f"   Path: {' -> '.join(path)}")
    
    return "\n".join(results)


def main():
    parser = argparse.ArgumentParser(description="Find shortest paths using Dijkstra's algorithm")
    parser.add_argument('input_file', help='Input file containing graph data')
    parser.add_argument('--start', '-s', required=True, help='Start vertex')
    parser.add_argument('--end', '-e', help='End vertex (optional, shows all if not specified)')
    parser.add_argument('--output', '-o', help='Output file for results')
    parser.add_argument('--visualize', '-v', action='store_true', 
                       help='Show graph visualization')
    
    args = parser.parse_args()
    
    # Check if input file exists
    if not os.path.exists(args.input_file):
        print(f"Error: Input file '{args.input_file}' not found!")
        sys.exit(1)
    
    # Load graph from file
    try:
        graph = load_graph_from_file(args.input_file)
        print(f"Graph loaded successfully from '{args.input_file}'")
    except Exception as e:
        print(f"Error loading graph: {e}")
        sys.exit(1)
    
    # Validate start vertex
    if args.start not in graph.vertices:
        print(f"Error: Start vertex '{args.start}' not found in graph!")
        print(f"Available vertices: {sorted(graph.vertices)}")
        sys.exit(1)
    
    # Run Dijkstra's algorithm
    print(f"Running Dijkstra's algorithm from vertex '{args.start}'...")
    distances, predecessors = dijkstra(graph, args.start)
    
    # Build results text
    results_text = build_results_text(graph, args.start, distances, predecessors, args.end)
    
    # Show visualization if requested
    if args.visualize:
        if args.end and args.end in graph.vertices and distances[args.end] != float('inf'):
            # Show specific path visualization
            path = graph.reconstruct_path(predecessors, args.start, args.end)
            if path:
                visualize_path_with_info(
                    graph, path, results_text,
                    title=f"Dijkstra: {args.start} to {args.end}"
                )
        else:
            # Show complete Dijkstra results
            visualize_dijkstra_complete(
                graph, args.start, distances, predecessors, results_text
            )
    else:
        # Just print to console if no visualization requested
        print(results_text)
    
    # Save results if output file specified
    if args.output:
        # Prepare results for file saving
        results = {
            'start': args.start,
            'distances': {},
            'paths': {}
        }
        
        for vertex in graph.vertices:
            if distances[vertex] == float('inf'):
                results['distances'][vertex] = 'No path'
            else:
                results['distances'][vertex] = distances[vertex]
                path = graph.reconstruct_path(predecessors, args.start, vertex)
                results['paths'][vertex] = path
        
        save_results(results, args.output, graph)
        print(f"\nResults saved to '{args.output}'")
    
    print("\nDone!")


if __name__ == "__main__":
    main()