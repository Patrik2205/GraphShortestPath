# Graph Shortest Path Algorithms

Implementation of classic shortest path algorithms for graphs.

## Algorithms Implemented

1. **Dijkstra's Algorithm** - For graphs with non-negative edges
2. **Bellman-Ford Algorithm** - Handles negative edges and detects negative cycles
3. **Floyd-Warshall Algorithm** - Computes all pairs shortest paths

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py <input_file> [options]

Options:
  -o, --output FILE     Save results to file
  -v, --visualize       Show graph visualization
```

### Example

```bash
# Run Dijkstra on the example graph with visualization
python main.py tests/image_graph.txt -v

# Run with output file
python main.py tests/test_data.txt -o output/results.txt
```

## Input Format

### Edge List Format
```
undirected
vertex1 vertex2 weight
vertex1 vertex3 weight
...
```

### JSON Format
```json
{
  "directed": false,
  "edges": [
    {"from": "A", "to": "B", "weight": 5},
    ...
  ]
}
```

## Test Files

- `tests/image_graph.txt` - Graph from the provided image
- `tests/test_data.txt` - General test data
- `tests/negative_edges.txt` - Graph with negative edges for Bellman-Ford
- `tests/czech_cities.json` - Real-world example with Czech cities
