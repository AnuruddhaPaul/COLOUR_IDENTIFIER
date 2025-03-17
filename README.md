# Capacitated Vehicle Routing Problem (CVRP) Solver


This project implements a greedy algorithm to solve the Capacitated Vehicle Routing Problem (CVRP). The solver finds efficient routes for visiting multiple locations while considering weight/capacity constraints and maximizing prize collection.

---

## Table of Contents
- [Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Explanation](#algorithm-explanation)
- [Code Explanation](#code-explanation)
- [Customization](#customization)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Overview
This project solves a variation of the Vehicle Routing Problem where:

- A vehicle must visit a set of locations starting and ending at a depot (node 0)
- Each location has an associated weight and prize
- The vehicle has a maximum carrying capacity
- The goal is to create efficient routes that respect the capacity constraint while collecting prizes

The solver generates multiple routes as needed to visit all locations, visualizes these routes, and tracks performance metrics.

---

## Requirements
Ensure you have the following installed:

- Python 3.6+
- NumPy
- Matplotlib
- Random (standard library)

---

## Installation
Clone this repository:

```bash
git clone https://github.com/yourusername/cvrp-solver.git
cd cvrp-solver
```

Install the required dependencies:

```bash
pip install numpy matplotlib
```

---

## Usage
Run the main script:

```bash
python cvrp_solver.py
```

The script will:

- Generate optimal routes considering capacity constraints
- Display the routes on a coordinate plot
- Show cost metrics across generations
- Print route details and prize totals to the console

---

## Algorithm Explanation
This implementation uses a greedy nearest-neighbor algorithm with capacity constraints:

1. Start from the depot (node 0)
2. Choose the nearest unvisited node that doesn't exceed capacity when added
3. Move to that node and repeat until no more nodes can be added
4. Return to the depot and start a new route if needed
5. Continue until all nodes are visited

The algorithm balances minimizing travel distance while respecting the maximum vehicle capacity of 200 units.

---

## Code Explanation

### Data Initialization:
```python
locations = np.array([...])  # [x,y] coordinates for each location
weights = np.array([...])    # Weight of items at each location
prizes = np.array([...])     # Prize value of each location
capacity = 200               # Maximum vehicle capacity
```

### Distance Calculation:
```python
def calculate_distance_matrix(locations):
    return np.linalg.norm(locations[:, None] - locations[None,:], axis=2)
```
Calculates Euclidean distances between all location pairs.

### Route Generation:
```python
while len(visited_all_nodes) < len(locations)-1:
    # Route building logic
    for next_node in range(1,len(locations)):
        if next_node not in visited_all_nodes:
            weight_if_visited = total_weight + weights[next_node]
            if weight_if_visited <= capacity:
                # Select node with shortest distance
```
Builds routes one at a time, respecting capacity constraints.

### Visualization:
```python
def plot_routes(locations, routes, total_prizes):
    # Plotting logic
```
Visualizes routes on a coordinate plane with different colors.

Tracks and displays prizes collected per route.

### Performance Tracking:
```python
best_cost_history.append(total_cost)
average_cost_history = [...]
```
Records performance metrics across route generations.

---

## Customization
You can modify the following parameters to adapt the solver to different scenarios:

### Location Data:
```python
# Change these arrays to define your own problem instances
locations = np.array([...])
weights = np.array([...])
prizes = np.array([...])
```

### Capacity Constraint:
```python
capacity = 200  # Change to adjust vehicle capacity
```

### Randomization Seed:
```python
random.seed(42)  # Change for different random behaviors
```

### Optimization Criteria:
You can modify the node selection logic to consider different factors:
```python
# Current: Selects nearest node
if distance_to_next < best_next_distance:
    
# Alternative: Consider prize/distance ratio
# if prizes[next_node]/distance_to_next > best_ratio:
```

---

## Troubleshooting
| Issue | Solution |
|--------|----------|
| No feasible routes found | Increase capacity or decrease weights |
| Poor route quality | Adjust node selection criteria or implement meta-heuristics |
| Performance issues | Reduce problem size or optimize distance calculations |
| Visualization errors | Check matplotlib installation and compatibility |

---



_Last updated: March 17, 2025_
