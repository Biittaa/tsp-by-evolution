import math
def create_distnce_matrix(input_path: str):
    # TODO: read data from file and create distance matrix

    with open(input_path,'r') as file:
        city_positions = [
            tuple(map(int,line.strip().split(','))) for line in file
        ]
    print("city positions:")
    print(city_positions) 
    print()

    city_count = len(city_positions) 

    distance_matrix = [[0.0]* city_count for _ in range(city_count)]

    for i in range(city_count):
        for j in range(city_count):
            x1 , y1 = city_positions[i]
            x2 , y2 = city_positions[j]
            distance_matrix[i][j] =   math.sqrt ((x1-x2)**2 + (y1-y2)**2)


    print("Distance Matrix:")
    print(distance_matrix)        

    return distance_matrix

