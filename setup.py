#!/usr/bin/env python3
"""
Setup script for Dijkstra's algorithm project
"""

import os
from src.file_handler import create_example_files


def create_directories():
    """Create necessary directories"""
    directories = ['src', 'tests', 'documentation', 'output']
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")


def create_requirements():
    """Create requirements.txt"""
    requirements = """matplotlib>=3.5.0
networkx>=2.6.0
numpy>=1.21.0
"""
    
    with open('requirements.txt', 'w') as f:
        f.write(requirements)
    print("Created: requirements.txt")


def create_readme():
    """Create README"""
    readme = """# Dijkstra's Shortest Path Algorithm

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
python main.py tests/czech_cities.txt -s Praha -e Ostrava -v
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
- `tests/czech_cities.txt` - Real-world example with Czech cities
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
"""
    
    with open('README.md', 'w') as f:
        f.write(readme)
    print("Created: README.md")


def create_gitignore():
    """Create .gitignore"""
    gitignore = """# Python
__pycache__/
*.py[cod]
*$py.class
.Python
venv/
env/
.env

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db

# Output
output/
*.png
*.jpg
*.pdf

# Temporary
*.tmp
.cache/
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore)
    print("Created: .gitignore")


def main():
    """Run setup"""
    print("Setting up Dijkstra's Algorithm project...")
    print("=" * 50)
    
    create_directories()
    print()
    
    # Create __init__.py files
    for directory in ['src']:
        init_file = os.path.join(directory, '__init__.py')
        with open(init_file, 'w') as f:
            f.write('# Package initialization\n')
        print(f"Created: {init_file}")
    
    print()
    create_example_files()
    print()
    create_requirements()
    create_readme()
    create_gitignore()
    
    print("\n" + "=" * 50)
    print("Setup complete!")
    print("\nNext steps:")
    print("1. Install requirements: pip install -r requirements.txt")
    print("2. Run example: python main.py tests/image_graph.txt -s 1 -v")
    print("3. See all options: python main.py -h")


if __name__ == "__main__":
    main()