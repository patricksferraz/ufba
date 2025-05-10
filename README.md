# UFBA

This repository contains abstracts, code, and study materials for projects developed at UFBA (Federal University of Bahia). It showcases various algorithms and implementations in graph handling, string manipulation, and artificial intelligence.

## Overview

This repository is a collection of projects that demonstrate different algorithms and techniques in computer science. Each project is designed to be educational and practical, providing a hands-on approach to understanding complex concepts.

## Projects

### Graph Handling

The `graph-handling` project focuses on graph algorithms and data structures. It includes implementations for:

- **Graph Class**: A class to represent and manipulate graphs.
- **Node Class**: A class to represent nodes in a graph.
- **Maximum Independent Set (MIS)**: An algorithm to find the maximum independent set in a graph.

### String Handling

The `string-handling` project provides utilities for string manipulation. It includes:

- **Accent Removal**: A function to remove accents from strings.
- **Palindrome Detection**: A function to find palindromes in a string.
- **Letter Counting**: A function to count occurrences of letters in a string.

### Artificial Intelligence

The `ia` project contains various AI algorithms, including:

- **A* Search**: An implementation of the A* search algorithm.
- **Naive Bayes**: A simple implementation of the Naive Bayes classifier.
- **Decision Tree ID3**: An implementation of the ID3 algorithm for decision trees.
- **Hill Climbing**: An implementation of the hill climbing algorithm.
- **Breadth-First Search**: An implementation of the breadth-first search algorithm.
- **Depth-First Search**: Implementations of both pre-order and post-order depth-first search.
- **Backward Chaining**: An implementation of the backward chaining algorithm.
- **Minimax**: An implementation of the minimax algorithm for game theory.

## Features

- **Modular Design**: Each project is modular and can be used independently.
- **Educational**: The projects are designed to be educational and provide a hands-on approach to learning.
- **Open Source**: The code is open source and available for anyone to use and modify.

## Usage

### Graph Handling

```python
from graph import Graph
from node import Node

# Create a graph
graph = Graph()

# Add nodes
node1 = Node("A", ["B", "C"])
node2 = Node("B", ["A", "C"])
graph.add_node(node1)
graph.add_node(node2)

# Print the graph
print(graph)
```

### String Handling

```python
from string_handling import find, format

# Remove accents
text = "áéíóú"
print(format.del_accents(text))  # Output: aeiou

# Find palindromes
msg = "arara"
print(find.palindromes(msg))  # Output: {'arara': 1}

# Count letters
str = "hello"
print(find.letters(str, 'l'))  # Output: {'l': 2}
```

### Artificial Intelligence

Each AI project has its own usage examples, which can be found in the respective directories.

## License

This project is licensed under the MIT License. See the [LICENSE](string-handling/LICENSE) file for more details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
