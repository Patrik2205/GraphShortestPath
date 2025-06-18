"""
Graph visualization for Dijkstra's algorithm
"""

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Patch
import textwrap


def create_figure_with_text():
    """Create a figure with graph and text areas"""
    fig = plt.figure(figsize=(16, 10))
    
    # Create grid layout: left side for graph, right side for text
    gs = fig.add_gridspec(1, 2, width_ratios=[3, 2], hspace=0.1, wspace=0.1)
    
    # Graph subplot
    ax_graph = fig.add_subplot(gs[0, 0])
    
    # Text subplot
    ax_text = fig.add_subplot(gs[0, 1])
    ax_text.axis('off')
    
    return fig, ax_graph, ax_text


def add_text_to_plot(ax_text, text_content, title="Results"):
    """Add text content to the text area of the plot"""
    ax_text.clear()
    ax_text.axis('off')
    
    # Title
    ax_text.text(0.5, 0.98, title, fontsize=16, weight='bold', 
                ha='center', va='top', transform=ax_text.transAxes)
    
    # Content
    ax_text.text(0.05, 0.92, text_content, fontsize=11, 
                ha='left', va='top', transform=ax_text.transAxes,
                family='monospace', wrap=True)


def visualize_graph_with_info(graph, results_text, title="Graph", highlight_edges=None, save_path=None):
    """Visualize the graph with information panel
    
    Args:
        graph: Graph object
        results_text: Text to display in the info panel
        title: Title for the plot
        highlight_edges: List of (u, v) tuples to highlight
        save_path: Path to save the figure (optional)
    """
    fig, ax_graph, ax_text = create_figure_with_text()
    
    # Create NetworkX graph
    if graph.directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    
    # Add edges
    for u, v, weight in graph.get_edges():
        G.add_edge(u, v, weight=weight)
    
    # Use spring layout for better visualization
    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=1500, alpha=0.9, ax=ax_graph)
    
    # Draw node labels
    nx.draw_networkx_labels(G, pos, font_size=16, font_weight='bold', ax=ax_graph)
    
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
                             arrowsize=20, arrowstyle='->', ax=ax_graph)
    else:
        nx.draw_networkx_edges(G, pos, edge_color=edge_colors, 
                             width=edge_widths, alpha=0.7, ax=ax_graph)
    
    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=12, ax=ax_graph)
    
    ax_graph.set_title(title, fontsize=16, fontweight='bold', pad=20)
    ax_graph.axis('off')
    
    # Add text to the right panel
    add_text_to_plot(ax_text, results_text, "Algorithm Output")
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


def visualize_path_with_info(graph, path, results_text, title="Dijkstra's Shortest Path", save_path=None):
    """Visualize a specific path in the graph with information panel
    
    Args:
        graph: Graph object
        path: List of vertices representing the path
        results_text: Text to display in the info panel
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
    
    visualize_graph_with_info(graph, results_text, title, highlight_edges, save_path)


def visualize_dijkstra_complete(graph, start, distances, predecessors, results_text, save_path=None):
    """Visualize the complete result of Dijkstra's algorithm with all information
    
    Args:
        graph: Graph object
        start: Start vertex
        distances: Dictionary of distances from Dijkstra
        predecessors: Dictionary of predecessors from Dijkstra
        results_text: Text to display in the info panel
        save_path: Path to save the figure (optional)
    """
    fig, ax_graph, ax_text = create_figure_with_text()
    
    # Create NetworkX graph
    if graph.directed:
        G = nx.DiGraph()
    else:
        G = nx.Graph()
    
    # Add edges
    for u, v, weight in graph.get_edges():
        G.add_edge(u, v, weight=weight)
    
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
                          node_size=1500, alpha=0.9, ax=ax_graph)
    
    # Create node labels with distances
    node_labels = {}
    for vertex in G.nodes():
        if distances[vertex] == float('inf'):
            node_labels[vertex] = f"{vertex}\n(∞)"
        else:
            node_labels[vertex] = f"{vertex}\n({distances[vertex]})"
    
    nx.draw_networkx_labels(G, pos, node_labels, font_size=12, ax=ax_graph)
    
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
                             arrowsize=20, arrowstyle='->', ax=ax_graph)
    else:
        nx.draw_networkx_edges(G, pos, edge_color=edge_colors, 
                             width=edge_widths, alpha=0.7, ax=ax_graph)
    
    # Draw edge labels
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10, ax=ax_graph)
    
    ax_graph.set_title(f"Dijkstra's Algorithm from '{start}'", fontsize=16, fontweight='bold', pad=20)
    ax_graph.axis('off')
    
    # Add legend
    legend_elements = [
        Patch(facecolor='green', label='Start vertex'),
        Patch(facecolor='lightblue', label='Reachable vertices'),
        Patch(facecolor='red', label='Unreachable vertices'),
    ]
    ax_graph.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0, 1))
    
    # Add text to the right panel
    add_text_to_plot(ax_text, results_text, "Dijkstra's Results")
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    plt.show()


# Keep old functions for backward compatibility but mark as deprecated
def visualize_graph(graph, title="Graph", highlight_edges=None, save_path=None):
    """[DEPRECATED] Use visualize_graph_with_info instead"""
    # Create dummy text
    stats = graph.get_graph_stats()
    results_text = f"Graph Statistics:\n"
    results_text += f"Vertices: {stats['num_vertices']}\n"
    results_text += f"Edges: {stats['num_edges']}\n"
    results_text += f"Type: {'Directed' if stats['directed'] else 'Undirected'}\n"
    
    visualize_graph_with_info(graph, results_text, title, highlight_edges, save_path)


def visualize_path(graph, path, title="Dijkstra's Shortest Path", save_path=None):
    """[DEPRECATED] Use visualize_path_with_info instead"""
    if not path or len(path) < 2:
        print("Cannot visualize path with less than 2 vertices")
        return
    
    # Create path info text
    results_text = f"Path: {' -> '.join(path)}\n"
    
    visualize_path_with_info(graph, path, results_text, title, save_path)


def visualize_dijkstra_progress(graph, start, distances, predecessors, save_path=None):
    """[DEPRECATED] Use visualize_dijkstra_complete instead"""
    # Create results text
    results_text = f"Start vertex: {start}\n\n"
    results_text += "Shortest distances:\n"
    results_text += "-" * 30 + "\n"
    
    for vertex in sorted(graph.vertices):
        if distances[vertex] == float('inf'):
            results_text += f"{start} -> {vertex}: No path\n"
        else:
            results_text += f"{start} -> {vertex}: {distances[vertex]}\n"
    
    visualize_dijkstra_complete(graph, start, distances, predecessors, results_text, save_path)