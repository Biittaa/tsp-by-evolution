from individual import Individual
import random

def select_two_individual_for_crossover(
    individual_list: list[Individual], population_size: int
) -> tuple[Individual, Individual]: # you can change return type based on your implementation
    # TODO: this method selects two individuals for the crossover algorithm

    total_fitness = sum(ind.fitness for ind in individual_list)

    # Compute the selection probabilities based on fitness
    selection_probabilities = [ind.fitness / total_fitness for ind in individual_list]
    
    selected = []
    for _ in range(2):  # We need to select two individuals
        random_point = random.uniform(0, 1)  # Generate a random point for selection
        cumulative_fitness = 0
        
        # Loop through the population to accumulate cumulative fitness
        for i, ind in enumerate(individual_list):
            cumulative_fitness += selection_probabilities[i]
            if random_point <= cumulative_fitness:  # Select when the random point is in the range
                selected.append(individual_list[i])
                break  # Once an individual is selected, exit the loop
    ind_tuple = (selected[0],selected[1])
    return ind_tuple

def next_generation_selection (population : list[Individual],generated_individuals : list[Individual],population_size:int):
    
    combined_population =  generated_individuals + population
    combined_population.sort(key=lambda ind: ind.fitness)
    next_generation = combined_population[:population_size]
    return next_generation





































    # total_fitness = sum(ind.fitness for ind in individual_list)

    # # Compute selection probabilities
    # selection_probabilities = [ind.fitness / total_fitness for ind in individual_list]
    
    # selected = []
    # for _ in range(2):
    #    random_point = random.uniform(0, 1)
    #    i=-1
    #    cumulative_fitness = 0
    #    for _ in individual_list:
    #        i = i + 1
    #        fitness = selection_probabilities[i]
    #        cumulative_fitness += fitness
    #        if random_point <= cumulative_fitness:
    #          selected.append(individual_list[i])
    #          break
    # return selected[0],selected[1]