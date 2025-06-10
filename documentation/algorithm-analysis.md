# Dijkstra's Algorithm Analysis

## Algorithm Overview

Dijkstra's algorithm is a greedy algorithm that finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative edge weights.

## Time Complexity

| Implementation | Time Complexity | Notes |
|----------------|-----------------|-------|
| With Binary Heap | O((V + E) log V) | Most common implementation |
| With Fibonacci Heap | O(E + V log V) | Better for dense graphs |
| With Array | O(V²) | Simple but slower |

Where:
- V = number of vertices
- E = number of edges

## Space Complexity

O(V) - for storing distances and predecessors

## Algorithm Steps

1. **Initialize**:
   - Set distance to source = 0
   - Set all other distances = ∞
   - Create priority queue with (0, source)

2. **Main Loop**:
   - Extract vertex with minimum distance
   - For each unvisited neighbor:
     - Calculate new distance through current vertex
     - If shorter, update distance and predecessor
     - Add to priority queue

3. **Termination**:
   - When all vertices processed or queue empty

## Performance Characteristics

### Best Case
- Sparse graphs (E ≈ V)
- Non-negative edge weights
- Single-source queries

### Worst Case
- Dense graphs (E ≈ V²)
- Many equal-weight paths

### Optimization Tips

1. **Early Termination**: If finding path to specific vertex, stop when target reached
2. **Bidirectional Search**: Search from both endpoints for point-to-point queries
3. **Preprocessing**: For multiple queries on same graph, consider preprocessing

## Practical Performance

### Small Graphs (< 100 vertices)
- Execution time: < 1ms
- Memory usage: Negligible

### Medium Graphs (100-1,000 vertices)
- Execution time: 1-10ms
- Memory usage: < 1MB

### Large Graphs (> 10,000 vertices)
- Execution time: 10-100ms
- Memory usage: Several MB

## Common Applications

1. **GPS Navigation**: Finding shortest routes
2. **Network Routing**: Internet packet routing
3. **Game AI**: Pathfinding in games
4. **Social Networks**: Finding degrees of separation
5. **Flight Planning**: Finding cheapest flights

## Limitations

1. **Cannot handle negative edges**: Will produce incorrect results
2. **Single-source only**: Must run V times for all-pairs
3. **Memory usage**: Requires storing entire graph

## Implementation Notes

### Priority Queue Choice
- **Binary Heap**: Good general-purpose choice
- **Fibonacci Heap**: Theoretical improvement, complex implementation
- **Simple Array**: Only for very small graphs

### Graph Representation
- **Adjacency List**: Best for sparse graphs
- **Adjacency Matrix**: Can be faster for dense graphs

### Practical Optimizations
```python
# Use visited set to avoid reprocessing
visited = set()

# Early termination for point-to-point
if current == target:
    break

# Preallocate data structures
distances = [float('inf')] * n
```