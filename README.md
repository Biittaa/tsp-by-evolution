# University Project: Solving the Traveling Salesman Problem using Evolutionary Algorithms
The Traveling Salesman Problem (TSP) is a classic problem in optimization, where the objective is to find the shortest possible route that visits a set of cities exactly once and returns to the origin.This project applies evolutionary algorithms (genetic algorithms) to explore possible solutions and improve them iteratively, leveraging the principles of natural evolution.

This solver aims to provide an efficient approach to TSP by mimicking processes like mutation, crossover, and selection in nature.
# Algoritm overview
The evolutionary algorithm implemented in this project consists of the following steps:

- Initialization: A population of random solutions (routes) is generated.

- Selection: The best individuals (routes) from the population are selected based on their fitness (shortest total distance).

- Crossover: Selected individuals undergo crossover to combine their genetic material (routes) and produce offspring with potential new solutions.

- Mutation: The offspring undergo mutation, where small random changes are made to the route to introduce genetic diversity.

- Replacement: The new population of offspring replaces the old population, and the process repeats for a set number of generations.
- 
# Setup
Ensure the following are installed on your system:
- Python 3.x
- Required library:
  ```bash
   pip install numpy matplotlib 
Clone the repository to your local machine:
  ```bash
    git clone https://github.com/Biittaa/tsp-by-evolution.git
  ```
Once you have cloned the repository and installed the dependencies, you can run the main algorithm.

Run the main script:
```bash
    python main.py
```
The algorithm will execute, solve the TSP problem using the evolutionary approach, and output the optimized route.

# Acknowledgments
- This project is part of the computation ai course.
- References and inspiration from works in genetic algorithms and optimization.

# Authors
- [Bita Asheghie](https://github.com/Biittaa)
