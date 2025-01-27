from individual import Individual
import random

def cross_over(parent1: Individual, parent2: Individual):
    
    genome_length = len(parent1.genome)
    cross_point_one = random.randint(0, genome_length-1)
    cross_point_two = random.randint(cross_point_one+1,genome_length)

    offspring1 = [None] * genome_length
    offspring2 =[None] * genome_length

    offspring1 [cross_point_one:cross_point_two] = parent1.genome[cross_point_one:cross_point_two]
    offspring2 [cross_point_one:cross_point_two] = parent2.genome[cross_point_one:cross_point_two]

    current_position = cross_point_two

    for city in parent2.genome:
        if city not in offspring1:
            if current_position == genome_length:
                current_position = 0
            offspring1[current_position] = city
            current_position +=1

    current_position = cross_point_two

    for city in parent1.genome:
        if city not in offspring2:
            if current_position == genome_length:
                current_position = 0
            offspring2[current_position] = city
            current_position +=1    
    
    offspring_ind_1 = Individual(genome_length=genome_length,generate_random_genome=False)
    offspring_ind_1.genome = offspring1

    offspring_ind_2 = Individual(genome_length=genome_length,generate_random_genome=False)
    offspring_ind_2.genome = offspring2
    return offspring_ind_1,offspring_ind_2
    