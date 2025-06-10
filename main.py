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
from src.visualization import visualize_graph, visualize_path
from src.file_handler import load_graph_from_file, save_results


def print_header():
    """Print application header"""
    print("=" * 60)
    print("Dijkstra's Shortest Path Algorithm".center(60))
    print("=" * 60)
    print()


def print_path(path, distance, start, end):
    """Print the shortest path result"""
    if path is None:
        print(f"\nNo path exists from {start} to {end}")
    else:
        print(f"\nShortest path from {start} to {end}:")
        print(f"Path: {' -> '.join(map(str, path))}")
        print(f"Total distance: {distance}")


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
    
    print_header()
    
    # Load graph from file
    try:
        graph = load_graph_from_file(args.input_file)
        print(f"Graph loaded successfully from '{args.input_file}'")
        print(f"Vertices: {sorted(graph.vertices)}")
        print(f"Number of edges: {len(graph.get_edges())}")
    except Exception as e:
        print(f"Error loading graph: {e}")
        sys.exit(1)
    
    # Check for negative edges
    if graph.has_negative_edges():
        print("\nWarning: Graph contains negative edges!")
        print("Dijkstra's algorithm may not produce correct results.")
        response = input("Continue anyway? (y/n): ")
        if response.lower() != 'y':
            sys.exit(0)
    
    # Validate start vertex
    if args.start not in graph.vertices:
        print(f"\nError: Start vertex '{args.start}' not found in graph!")
        print(f"Available vertices: {sorted(graph.vertices)}")
        sys.exit(1)
    
    # Show initial visualization if requested
    if args.visualize:
        visualize_graph(graph, title="Input Graph")
    
    # Run Dijkstra's algorithm
    print(f"\nRunning Dijkstra's algorithm from vertex '{args.start}'...")
    distances, predecessors = dijkstra(graph, args.start)
    
    # Prepare results
    results = {
        'start': args.start,
        'distances': {},
        'paths': {}
    }
    
    # Display results
    print(f"\nShortest distances from '{args.start}':")
    print("-" * 40)
    
    for vertex in sorted(graph.vertices):
        if distances[vertex] == float('inf'):
            print(f"{args.start} -> {vertex}: No path")
            results['distances'][vertex] = 'No path'
        else:
            print(f"{args.start} -> {vertex}: {distances[vertex]}")
            results['distances'][vertex] = distances[vertex]
            
            # Reconstruct path
            path = graph.reconstruct_path(predecessors, args.start, vertex)
            results['paths'][vertex] = path
    
    # Show specific path if end vertex specified
    if args.end:
        if args.end not in graph.vertices:
            print(f"\nError: End vertex '{args.end}' not found in graph!")
        else:
            path = graph.reconstruct_path(predecessors, args.start, args.end)
            print_path(path, distances[args.end], args.start, args.end)
            
            if args.visualize and path:
                visualize_path(graph, path, 
                             title=f"Dijkstra: {args.start} to {args.end}")
    
    # Save results if output file specified
    if args.output:
        save_results(results, args.output, graph)
        print(f"\nResults saved to '{args.output}'")
    
    print("\nDone!")


if __name__ == "__main__":
    main()