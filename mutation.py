from individual import Individual
import random

def mutation1(individual: Individual):
    # TODO: this method applies mutation on an individual

    genome_length = len(individual.genome)
    
    position_one = random.randint(0,genome_length-1)
    position_two = random.randint(0,genome_length-1)

    while position_one == position_two :
         position_two = random.randint(0,genome_length-1)
    
    individual.genome[position_one],individual.genome[position_two] = individual.genome[position_two],individual.genome[position_one]
    
    return individual