"""
Graph data structure for Dijkstra's algorithm
"""

from collections import defaultdict


class Graph:
    """Graph class for Dijkstra's shortest path algorithm"""
    
    def __init__(self, directed=False):
        """Initialize graph
        
        Args:
            directed (bool): True for directed graph, False for undirected
        """
        self.adj_list = defaultdict(list)
        self.vertices = set()
        self.directed = directed
    
    def add_edge(self, u, v, weight):
        """Add an edge to the graph
        
        Args:
            u: Start vertex
            v: End vertex
            weight: Edge weight (should be non-negative for Dijkstra)
        """
        self.adj_list[u].append((v, weight))
        self.vertices.add(u)
        self.vertices.add(v)
        
        if not self.directed:
            self.adj_list[v].append((u, weight))
    
    def get_neighbors(self, vertex):
        """Get all neighbors of a vertex
        
        Args:
            vertex: The vertex to get neighbors for
            
        Returns:
            List of (neighbor, weight) tuples
        """
        return self.adj_list[vertex]
    
    def get_edges(self):
        """Get all edges in the graph
        
        Returns:
            List of (u, v, weight) tuples
        """
        edges = []
        seen = set()
        
        for u in self.adj_list:
            for v, weight in self.adj_list[u]:
                if self.directed:
                    edges.append((u, v, weight))
                else:
                    # For undirected graphs, avoid duplicates
                    edge = tuple(sorted([u, v]))
                    if edge not in seen:
                        edges.append((u, v, weight))
                        seen.add(edge)
        
        return edges
    
    def has_negative_edges(self):
        """Check if graph has negative edges
        
        Returns:
            bool: True if graph has negative edges
        """
        for u in self.adj_list:
            for v, weight in self.adj_list[u]:
                if weight < 0:
                    return True
        return False
    
    def reconstruct_path(self, predecessors, start, end):
        """Reconstruct path from predecessors dictionary
        
        Args:
            predecessors: Dictionary of predecessors from Dijkstra
            start: Start vertex
            end: End vertex
            
        Returns:
            List representing the path, or None if no path exists
        """
        if predecessors[end] is None and start != end:
            return None
        
        path = []
        current = end
        
        while current is not None:
            path.append(current)
            if current == start:
                break
            current = predecessors[current]
        
        path.reverse()
        return path
    
    def get_graph_stats(self):
        """Get basic statistics about the graph
        
        Returns:
            Dictionary with graph statistics
        """
        edges = self.get_edges()
        total_weight = sum(weight for _, _, weight in edges)
        
        return {
            'num_vertices': len(self.vertices),
            'num_edges': len(edges),
            'directed': self.directed,
            'total_weight': total_weight,
            'average_weight': total_weight / len(edges) if edges else 0,
            'has_negative_edges': self.has_negative_edges()
        }