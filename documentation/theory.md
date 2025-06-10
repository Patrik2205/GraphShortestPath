# Dijkstra's Algorithm - Theoretical Foundation

## 1. Introduction

Dijkstra's algorithm, created by Edsger W. Dijkstra in 1956 and published in 1959, is one of the most important algorithms in computer science for finding shortest paths in graphs.

## 2. Problem Definition

### Single-Source Shortest Path (SSSP)
Given:
- A weighted graph G = (V, E)
- A source vertex s ∈ V
- Non-negative edge weights w(u,v) ≥ 0

Find: The shortest path from s to every other vertex in the graph

## 3. Algorithm Principle

### Greedy Approach
Dijkstra's algorithm uses a greedy strategy:
- Always process the unvisited vertex with the smallest known distance
- This guarantees that when a vertex is processed, we've found its shortest path

### Key Insight
For graphs with non-negative weights, the shortest path to a vertex v must go through vertices closer to the source than v.

## 4. Mathematical Foundation

### Optimal Substructure
If the shortest path from s to v goes through u, then:
- The subpath from s to u must also be a shortest path
- Distance(s,v) = Distance(s,u) + weight(u,v)

### Relaxation
The core operation that updates distances:
```
if distance[u] + weight(u,v) < distance[v]:
    distance[v] = distance[u] + weight(u,v)
    predecessor[v] = u
```

## 5. Algorithm Correctness

### Invariant
At any point during execution:
1. For all processed vertices, the computed distance is optimal
2. For unprocessed vertices, the computed distance is the shortest using only processed vertices

### Proof Sketch
1. Base case: distance[source] = 0 is optimal
2. Inductive step: When selecting the minimum unprocessed vertex, no shorter path exists
3. Conclusion: All distances are optimal when algorithm terminates

## 6. Why Non-Negative Weights?

### The Problem with Negative Edges
Consider this graph:
```
A --(-2)--> B
 \          |
  \----5----/
```
- Dijkstra might process B before exploring the path through A
- Would miss the shorter path A→B with cost -2

### Mathematical Reason
The algorithm assumes that adding edges to a path never decreases its length, which is false with negative weights.

## 7. Data Structures

### Priority Queue Requirements
- Insert: Add vertex with priority
- Extract-Min: Remove vertex with minimum distance
- Decrease-Key: Update vertex priority

### Implementation Options
1. **Array**: O(V) extract-min, O(1) decrease-key
2. **Binary Heap**: O(log V) for both operations
3. **Fibonacci Heap**: O(log V) extract-min, O(1) amortized decrease-key

## 8. Variants and Extensions

### Single-Pair Shortest Path
- Can terminate early when target reached
- Average case faster than full SSSP

### Bidirectional Dijkstra
- Run from both source and target
- Meet in the middle
- Can be 2x faster for point-to-point

### A* Algorithm
- Uses heuristic function h(v) estimating distance to target
- Priority = g(v) + h(v) where g(v) is distance from source
- Faster than Dijkstra for single-pair queries

## 9. Real-World Considerations

### Preprocessing
- For repeated queries on same graph
- Can precompute and store shortest path trees

### Dynamic Updates
- Handling edge weight changes
- Vertex additions/deletions
- Often requires partial recomputation

### Large-Scale Graphs
- Highway hierarchies for road networks
- Transit nodes
- Contraction hierarchies

## 10. Example Walkthrough

Consider finding shortest paths from vertex A:

```
Initial: A(0), B(∞), C(∞), D(∞)

Step 1: Process A
- Update B: 0 + 4 = 4
- Update C: 0 + 2 = 2
Queue: C(2), B(4), D(∞)

Step 2: Process C
- Update B: min(4, 2+1) = 3
- Update D: 2 + 8 = 10
Queue: B(3), D(10)

Step 3: Process B
- Update D: min(10, 3+5) = 8
Queue: D(8)

Step 4: Process D
Done! Shortest paths found.
```

## References

1. Dijkstra, E. W. (1959). "A note on two problems in connexion with graphs"
2. Cormen, T. H., et al. (2009). "Introduction to Algorithms" (3rd ed.)
3. Ahuja, R. K., et al. (1993). "Network Flows: Theory, Algorithms, and Applications"