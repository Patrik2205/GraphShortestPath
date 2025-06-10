"""
Graph visualization for Dijkstra's algorithm
"""

import matplotlib.pyplot as plt
import networkx as nx


def visualize_graph(graph, title="Graph", highlight_edges=None, save_path=None):
    """Visualize the graph
    
    Args:
        graph: Graph object
        title: Title for the plot
        highlight_edges: List of (u, v) tuples to highlight
        save_path: Path to save the figure (optional)
    """
    # Create NetworkX graph
    if graph.directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    
    # Add edges
    for u, v, weight in graph.get_edges():
        G.add_edge(u, v, weight=weight)
    
    # Create figure
    plt.figure(figsize=(10, 8))
    
    # Use spring layout for better visualization
    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=1500, alpha=0.9)
    
    # Draw node labels
    nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold')
    
    # Draw edges
    edge_colors = []
    edge_widths = []
    
    for u, v in G.edges():
        if highlight_edges and ((u, v) in highlight_edges or 
                               (v, u) in highlight_edges):
            edge_colors.append('red')
            edge_widths.append(3)
        else:
            edge_colors.append('gray')
            edge_widths.append(1)
    
    if graph.directed:
        nx.draw_networkx_edges(G, pos, edge_color=edge_colors, 
                             width=edge_widths, alpha=0.7,
                             arrowsize=20, arrowstyle='->')
    else:
        nx.draw_networkx_edges(G, pos, edge_color=edge_colors, 
                             width=edge_widths, alpha=0.7)
    
    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=12)
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def visualize_path(graph, path, title="Dijkstra's Shortest Path", save_path=None):
    """Visualize a specific path in the graph
    
    Args:
        graph: Graph object
        path: List of vertices representing the path
        title: Title for the plot
        save_path: Path to save the figure (optional)
    """
    if not path or len(path) < 2:
        print("Cannot visualize path with less than 2 vertices")
        return
    
    # Create highlight edges from path
    highlight_edges = []
    for i in range(len(path) - 1):
        highlight_edges.append((path[i], path[i + 1]))
    
    visualize_graph(graph, title, highlight_edges, save_path)


def visualize_dijkstra_progress(graph, start, distances, predecessors, save_path=None):
    """Visualize the result of Dijkstra's algorithm showing distances from start
    
    Args:
        graph: Graph object
        start: Start vertex
        distances: Dictionary of distances from Dijkstra
        predecessors: Dictionary of predecessors from Dijkstra
        save_path: Path to save the figure (optional)
    """
    # Create NetworkX graph
    if graph.directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    
    # Add edges
    for u, v, weight in graph.get_edges():
        G.add_edge(u, v, weight=weight)
    
    # Create figure
    plt.figure(figsize=(12, 8))
    
    # Use spring layout
    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
    
    # Color nodes based on distance
    node_colors = []
    for vertex in G.nodes():
        if vertex == start:
            node_colors.append('green')  # Start node
        elif distances[vertex] == float('inf'):
            node_colors.append('red')     # Unreachable
        else:
            node_colors.append('lightblue')  # Reachable
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, 
                          node_size=1500, alpha=0.9)
    
    # Create node labels with distances
    node_labels = {}
    for vertex in G.nodes():
        if distances[vertex] == float('inf'):
            node_labels[vertex] = f"{vertex}\n(∞)"
        else:
            node_labels[vertex] = f"{vertex}\n({distances[vertex]})"
    
    nx.draw_networkx_labels(G, pos, node_labels, font_size=12)
    
    # Highlight shortest path tree edges
    edge_colors = []
    edge_widths = []
    
    shortest_path_edges = set()
    for vertex in G.nodes():
        if predecessors[vertex] is not None:
            shortest_path_edges.add((predecessors[vertex], vertex))
    
    for u, v in G.edges():
        if (u, v) in shortest_path_edges or (v, u) in shortest_path_edges:
            edge_colors.append('blue')
            edge_widths.append(2.5)
        else:
            edge_colors.append('gray')
            edge_widths.append(1)
    
    if graph.directed:
        nx.draw_networkx_edges(G, pos, edge_color=edge_colors, 
                             width=edge_widths, alpha=0.7,
                             arrowsize=20, arrowstyle='->')
    else:
        nx.draw_networkx_edges(G, pos, edge_color=edge_colors, 
                             width=edge_widths, alpha=0.7)
    
    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10)
    
    plt.title(f"Dijkstra's Algorithm from '{start}'", fontsize=16, fontweight='bold')
    plt.axis('off')
    
    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='green', label='Start vertex'),
        Patch(facecolor='lightblue', label='Reachable vertices'),
        Patch(facecolor='red', label='Unreachable vertices'),
    ]
    plt.legend(handles=legend_elements, loc='upper right')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()