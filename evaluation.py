from individual import Individual


def evaluate_all(individual_list: list[Individual],distance_matrix):
    for individual in individual_list:
        evaluate(individual,distance_matrix)


def evaluate(individual: Individual,distance_matrix):
    # TODO: this method computes fitness (based on the TSP problem) and updates the fitness attribute of the individual parameter (individual.fitness=new_fitness)

    genome = individual.genome
    total_distance = 0

    num_genome = len(genome)

    for i in range(num_genome - 1):
        a = genome[i]
        b = genome[i+1]
        total_distance += distance_matrix[a][b]

    a = genome[0]
    b = genome[-1]
    total_distance += distance_matrix[a][b]    
    fitness = (total_distance)
    individual.fitness = fitness
    pass
