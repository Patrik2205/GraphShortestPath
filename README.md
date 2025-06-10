# Dijkstra's Shortest Path Algorithm

Implementation of Dijkstra's algorithm for finding shortest paths in graphs.

## About Dijkstra's Algorithm

Dijkstra's algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative edge weights. It uses a greedy approach with a priority queue.

- **Time Complexity**: O((V + E) log V) with binary heap
- **Space Complexity**: O(V)
- **Limitation**: Cannot handle negative edge weights

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py <input_file> -s <start_vertex> [options]

Required arguments:
  input_file          Path to graph file
  -s, --start         Start vertex for Dijkstra's algorithm

Optional arguments:
  -e, --end           End vertex (shows specific path)
  -o, --output        Save results to file
  -v, --visualize     Show graph visualization
  -h, --help          Show help message
```

### Examples

```bash
# Find shortest paths from vertex 1 in the example graph
python main.py tests/image_graph.txt -s 1

# Find path from 1 to 5 with visualization
python main.py tests/image_graph.txt -s 1 -e 5 -v

# Save results to file
python main.py tests/test_data.txt -s A -o output/results.txt

# Run on Czech cities example
python main.py tests/czech_cities.json -s Praha -e Ostrava -v
```

## Input Format

### Edge List Format
```
# Comments start with #
undirected
vertex1 vertex2 weight
vertex1 vertex3 weight
...
```

For directed graphs, use `directed` instead of `undirected`.

### JSON Format
```json
{
  "directed": false,
  "edges": [
    {"from": "A", "to": "B", "weight": 5},
    {"from": "B", "to": "C", "weight": 3}
  ]
}
```

## Test Files

- `tests/image_graph.txt` - Graph from the provided image (vertices 1-5)
- `tests/test_data.txt` - General test graph
- `tests/directed_graph.txt` - Example directed graph
- `tests/czech_cities.json` - Real-world example with Czech cities
- `tests/dijkstra_example.json` - JSON format example

## Project Structure

```
.
├── main.py                 # Main application
├── example.py              # Example usage
├── setup.py                # Setup script
├── requirements.txt        # Python dependencies
├── src/
│   ├── __init__.py
│   ├── graph.py           # Graph data structure
│   ├── dijkstra.py        # Dijkstra's algorithm
│   ├── visualization.py   # Graph visualization
│   └── file_handler.py    # File I/O operations
├── tests/                 # Test data files
├── documentation/         # Algorithm documentation
└── output/                # Output files
```

## Algorithm Details

Dijkstra's algorithm works by:
1. Starting with the source vertex at distance 0
2. Maintaining a priority queue of unvisited vertices
3. Always processing the closest unvisited vertex
4. Updating distances to neighbors (relaxation)
5. Continuing until all reachable vertices are processed

The algorithm guarantees finding the shortest path in graphs with non-negative edge weights.

## Visualization

The implementation includes graphical visualization features:
- **Original graph** - Shows the input graph structure
- **Shortest path** - Highlights a specific path in red
- **Complete solution** - Shows all shortest paths from source with distances

## Performance

- Small graphs (< 100 vertices): < 1ms
- Medium graphs (100-1,000 vertices): 1-10ms  
- Large graphs (> 10,000 vertices): 10-100ms

## Author

This implementation was created as part of a graph algorithms study project.