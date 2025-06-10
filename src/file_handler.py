"""
File handling for Dijkstra's algorithm
"""

import json
from datetime import datetime
from src.graph import Graph


def load_graph_from_file(filename):
    """Load graph from file
    
    Supported formats:
    - Edge list: u v weight (one edge per line)
    - JSON format
    
    Args:
        filename: Path to input file
        
    Returns:
        Graph object
    """
    with open(filename, 'r') as f:
        content = f.read().strip()
    
    # Try to parse as JSON first
    try:
        data = json.loads(content)
        return load_from_json(data)
    except json.JSONDecodeError:
        # Parse as edge list
        return load_from_edge_list(content)


def load_from_json(data):
    """Load graph from JSON data
    
    Expected format:
    {
        "directed": true/false,
        "edges": [
            {"from": "A", "to": "B", "weight": 5},
            ...
        ]
    }
    """
    graph = Graph(directed=data.get('directed', False))
    
    for edge in data['edges']:
        graph.add_edge(edge['from'], edge['to'], edge['weight'])
    
    return graph


def load_from_edge_list(content):
    """Load graph from edge list format
    
    Format: u v weight (one edge per line)
    First line can optionally be 'directed' or 'undirected'
    """
    lines = content.strip().split('\n')
    
    directed = False
    start_idx = 0
    
    # Check for directed/undirected specification
    if lines[0].lower() in ['directed', 'undirected']:
        directed = lines[0].lower() == 'directed'
        start_idx = 1
    
    graph = Graph(directed=directed)
    
    for line in lines[start_idx:]:
        line = line.strip()
        if not line or line.startswith('#'):  # Skip empty lines and comments
            continue
        
        parts = line.split()
        if len(parts) >= 3:
            u, v = parts[0], parts[1]
            weight = float(parts[2])
            graph.add_edge(u, v, weight)
    
    return graph


def save_results(results, filename, graph):
    """Save Dijkstra algorithm results to file
    
    Args:
        results: Dictionary with results
        filename: Output filename
        graph: Graph object
    """
    with open(filename, 'w') as f:
        f.write("Dijkstra's Shortest Path Algorithm Results\n")
        f.write("=" * 50 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Graph statistics
        stats = graph.get_graph_stats()
        f.write("Graph Information:\n")
        f.write(f"  Vertices: {stats['num_vertices']}\n")
        f.write(f"  Edges: {stats['num_edges']}\n")
        f.write(f"  Type: {'Directed' if stats['directed'] else 'Undirected'}\n")
        f.write(f"  Total weight: {stats['total_weight']}\n")
        f.write(f"  Average weight: {stats['average_weight']:.2f}\n\n")
        
        # Results
        f.write(f"Start vertex: {results['start']}\n\n")
        
        f.write("Shortest distances:\n")
        f.write("-" * 30 + "\n")
        
        for vertex in sorted(results['distances'].keys()):
            distance = results['distances'][vertex]
            if distance == 'No path':
                f.write(f"{results['start']} -> {vertex}: No path\n")
            else:
                f.write(f"{results['start']} -> {vertex}: {distance}\n")
                
                # Write path if available
                if vertex in results['paths'] and results['paths'][vertex]:
                    path = results['paths'][vertex]
                    f.write(f"   Path: {' -> '.join(path)}\n")
        
        f.write("\n")


def export_graph_to_json(graph, filename):
    """Export graph to JSON format
    
    Args:
        graph: Graph object
        filename: Output filename
    """
    data = {
        "directed": graph.directed,
        "vertices": sorted(list(graph.vertices)),
        "edges": []
    }
    
    for u, v, weight in graph.get_edges():
        data["edges"].append({
            "from": u,
            "to": v,
            "weight": weight
        })
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)


def create_example_files():
    """Create example test files for Dijkstra's algorithm"""
    
    # Example from the image
    example1 = """undirected
1 2 2
1 3 10
1 4 8
2 5 4
3 4 3
4 5 1
"""
    
    with open('tests/image_graph.txt', 'w') as f:
        f.write(example1)
    
    # Simple directed graph
    example2 = """directed
A B 5
A C 3
B C 2
B D 6
C D 7
C E 4
D E 1
D F 2
E F 3
"""
    
    with open('tests/directed_graph.txt', 'w') as f:
        f.write(example2)
    
    # Larger example
    example3 = """undirected
# Czech cities example
Praha Brno 205
Praha Plzen 91
Praha Pardubice 109
Brno Ostrava 169
Brno Pardubice 152
Plzen Ceske_Budejovice 144
Pardubice Hradec_Kralove 28
Hradec_Kralove Liberec 120
Ostrava Olomouc 93
Olomouc Brno 77
"""
    
    with open('tests/czech_cities.txt', 'w') as f:
        f.write(example3)
    
    # JSON example
    json_example = {
        "directed": False,
        "edges": [
            {"from": "S", "to": "A", "weight": 7},
            {"from": "S", "to": "B", "weight": 9},
            {"from": "S", "to": "F", "weight": 14},
            {"from": "A", "to": "B", "weight": 10},
            {"from": "A", "to": "C", "weight": 15},
            {"from": "B", "to": "C", "weight": 11},
            {"from": "B", "to": "F", "weight": 2},
            {"from": "C", "to": "D", "weight": 6},
            {"from": "D", "to": "E", "weight": 9},
            {"from": "E", "to": "F", "weight": 9}
        ]
    }
    
    with open('tests/dijkstra_example.json', 'w') as f:
        json.dump(json_example, f, indent=2)
    
    # Test data as specified
    test_data = """# Test graph for Dijkstra's algorithm
undirected

A B 4
A C 2
B C 1
B D 5
C D 8
C E 10
D E 2
D F 6
E F 3
"""
    
    with open('tests/test_data.txt', 'w') as f:
        f.write(test_data)