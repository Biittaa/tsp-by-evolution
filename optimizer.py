import random

from individual import Individual
from evaluation import evaluate, evaluate_all
from selection import select_two_individual_for_crossover,next_generation_selection
from crossover import cross_over
from mutation import mutation1
from termination_condition import terminate1


def run_algorithm(
    distance_matrix,
    population_size=20,
    generation_size=30,
):
    MUTATION_RATE = 0.3
    best_fitness_list = []
    avg_fitness_list = []
    best_individual = None
    genome_size = len(distance_matrix)
    
    # create primary population
    population = primary_population_creator(population_size, genome_size)
    evaluate_all(population,distance_matrix=distance_matrix)
    while True:
        # cross over
        generated_individuals = []
        for _ in range(int(generation_size / 2)):
            # TODO
            parent1 , parent2 = select_two_individual_for_crossover(population,population_size=population_size)

            offspring1 , offspring2 = cross_over(parent1=parent1,parent2=parent2)

            generated_individuals.extend([offspring1,offspring2])

            # pass


        # mutation
        for individual in generated_individuals:
            # TODO: by using a random number and 'MUTATION_RATE', decide whether to mutate the individual or not    
            random_number = random.randint(0,1)
            if random_number < MUTATION_RATE:
                mutation1(individual=individual)
            # pass
        
        # TODO: evaluate generated_individuals
        evaluate_all(generated_individuals,distance_matrix=distance_matrix)
        
        # TODO: select next generation by use of 'next_generation_selection' method
        selected_population = next_generation_selection(population=population,generated_individuals=generated_individuals,population_size=population_size)
        
        # TODO: check termination condition on generated individuals
        termination_output_individual =  terminate1(selected_population)
        if termination_output_individual:
            best_individual = termination_output_individual
            break


        # TODO: redefine 'population' for the next iteration
        population = selected_population
        # don't change following codes
        best_fitness_list.append(best_fitness(population))
        avg_fitness_list.append(avg_fitness(population))
        random.shuffle(population)
    
    return best_individual, best_fitness_list, avg_fitness_list

def primary_population_creator(
    population_size: int, genome_size: int
) -> list[Individual]:
    # TODO: this method create primary individual based on input population size and return them as list of individuals
    individual_list = []
    for _ in range(population_size):
        individual_list.append(Individual(genome_length=genome_size,generate_random_genome=True))
    return individual_list

def avg_fitness(
        population:list[Individual]
) -> float:
    # TODO: this method calculates average of individuals fitness
    total_fitness = 0
    for ind in population:
        total_fitness += (ind.fitness)
    return total_fitness / (len(population))    
    


def best_fitness(
        population:list[Individual]
) -> float:
    # TODO: this method finds best fitness in the population
    return max(ind.fitness for ind in population)
    