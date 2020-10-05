"""
Travelling Salesman problem (TSP):
    The travelling salesman problem (TSP) asks the following question: 
    "Given a list of cities and the distances between each pair of cities,
    what is the shortest possible route that visits each city exactly once and returns to the origin city?".
    For simplicity, we aren't coming back to origin city for now.
Genetic Algorithm:
    genetic algorithm (GA) is a metaheuristic inspired by the process of
     natural selection that belongs
     to the larger class of evolutionary algorithms (EA).
     Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems 
     by relying on biologically inspired operators such as mutation, crossover and selection.

I have written the same in Typescript where you can see everything visually..
It's available at https://dillir07.github.io/Genetic-Algorithm-TSP/
"""

function generate_cities(number_of_cities, map_limit)
    """
    Generates and returns given list of Cities (id, x-position, y-position)
    (x,y) positions are random taken below map_limit
    """
	cities = []
    for city_counter in 1:number_of_cities
        push!(cities, Dict("id" => city_counter, "x" => round(rand() * map_limit), "y" => round(rand() * map_limit)))
    end
	println("Cities Generated:", size(cities)[1])
	return cities
end


function shuffle_chromosome(chromosome)
    """
    Shuffles (Randomizes) the given chromosome
    """
    for i in 1:size(chromosome)[1]
        random_point = rand(chromosome)
        chromosome[i], chromosome[random_point] = chromosome[random_point], chromosome[i]
    end
    return chromosome
end


function calculate_distance_between_two_points(point1, point2)
    """
    Returns the distance between two cities (two points in a 2D plane)
    for more info ref: https://www.mathsisfun.com/algebra/distance-2-points.html
    """
    return sqrt((((point2[1] - point1[1]))^2) + (((point2[2] - point1[2]))^2))
end

function calculate_chromosome_travel_distance(chromosome)
    """
    Calculates the travel distance for given path/chromosome
    """
    travel_distance = 0
    for geneId in 1:size(chromosome)[1] - 1
        point1 = (cities[chromosome[geneId]]["x"], cities[chromosome[geneId]]["y"])
        point2 = (cities[chromosome[geneId + 1]]["x"], cities[chromosome[geneId + 1]]["y"])
        travel_distance += calculate_distance_between_two_points(point1, point2)
    end
    return travel_distance
end

function generate_initial_population(initial_population_size)
	"""
	Generates Initial Population
	"""
	chromosomes = []
    for population_counter in 1:initial_population_size
        chromosome = shuffle_chromosome(copy(initial_chromosome))
        calculate_chromosome_travel_distance(chromosome)
        push!(chromosomes, Dict("chromosome" => chromosome, "distance" => calculate_chromosome_travel_distance(chromosome)))

    end
	return chromosomes
end


function crossover(parent_one_chromosome, parent_two_chromosome, crossover_point)
    """
    Generates new offspring by doing a crossover between given two parents' chromosomes
    Using Uni-Point crossover method here, to be simpler.
    """
	offspring_part_one = parent_one_chromosome[1:crossover_point]
	for gene in offspring_part_one
		if gene in parent_two_chromosome
			gene_loc = findfirst(el -> el == gene, parent_two_chromosome)
			splice!(parent_two_chromosome, gene_loc)
		end
	end
	return vcat(offspring_part_one, parent_two_chromosome)
end


function mutate(offspring)
    """
    Mutates the given chromosome (offspring) by doing a swap of randomly choosen gene
    """
	random_mutation_point1 = rand(offspring)
	random_mutation_point2 = rand(offspring)
	offspring[random_mutation_point1], offspring[random_mutation_point2] = offspring[random_mutation_point2], offspring[random_mutation_point1]
	return offspring
end

function sort_chromosomes_in_place(chromosomes)
    """
    Sorts the whole population or chromosomes by sorting
    Chromosomes with less travel distance takes precendence
    """
    sort!(chromosomes, by=x -> x["distance"], rev=false)
end


function evolve(generation_count, offsprings_count, crossover_point)
	for generation in 1:generation_count
		for offspring_count in 1:offsprings_count
			random_parent_one_id = rand(1:size(chromosomes)[1])
            random_parent_two_id = rand(1:size(chromosomes)[1])
            random_parent_one = copy(chromosomes[random_parent_one_id]["chromosome"])
            random_parent_two = copy(chromosomes[random_parent_two_id]["chromosome"])
			offspring = crossover(random_parent_one, random_parent_two, crossover_point)
			offspring = mutate(offspring)
        	push!(chromosomes, Dict("chromosome" => offspring, "distance" => calculate_chromosome_travel_distance(offspring)))
        end
        sort_chromosomes_in_place(chromosomes)
        if (verbose_output)
            println("Generation #: $generation, offsprings processed: $(generation * offsprings_count), Best Score: $(chromosomes[1]["distance"]), Worst Score: $(chromosomes[size(chromosomes)[1]]["distance"])")
        end
		splice!(chromosomes, (offsprings_count + 1):size(chromosomes)[1])
	end
end

# make this true if you want best & bad scroes for each generation
verbose_output = false
# city map size
canvas_limit = 500

number_of_cities = 10
number_of_generations_allowed = 100
initial_population_size = 10
chromosomes = []
number_of_offsprings_allowed = 5

cities = generate_cities(number_of_cities, canvas_limit)
crossover_point = round(Int, size(cities)[1] / 2)
initial_chromosome = [1:number_of_cities;]
chromosomes = generate_initial_population(initial_population_size)
sort_chromosomes_in_place(chromosomes)
evolve(number_of_generations_allowed, number_of_offsprings_allowed, crossover_point)

println()
println("Best Path: $(chromosomes[1]["chromosome"])")
println("Best Score: $(chromosomes[1]["distance"])")