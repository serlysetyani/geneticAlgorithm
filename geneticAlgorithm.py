import math
import random
import copy

xLimit = [-1, 2]
yLimit = [-1, 1]
totalGen = 6
totalChromosome = 6
totalPopulation = 100
probability = 0.65
mutationProbability = 0.08

def initiate_chromosome(totalGen):           # fungsi untuk mengenerate chromosome
  chromosome = []                            # inisialisai array untuk chromosome
  for _ in range(totalGen):                  # perulangan untuk generate angka random pada tiap iterasinya
    chromosome.append(random.randint(0,9))
  return chromosome

def initiate_population(totalChromosome, totalGen):  # fungsi untuk mengenerate populasi
  population = []                                   # inisialisasi array untuk populasi
  for _ in range (totalChromosome):                  # perulangan untuk generate random populasi 
    chromosome = initiate_chromosome(totalGen)
    population.append(chromosome)
  return population

def decodeChromosome(chromosome, xLimit, yLimit):
    divider = 9 * (10**-1 + 10**-2 + 10**-3)
    multiplierX = chromosome[0] * (10**-1) + chromosome[1] * (10**-2) + chromosome[2] * (10**-3)
    multiplierY = chromosome[3] * (10**-1) + chromosome[4] * (10**-2) + chromosome[5] * (10**-3)
    decodeX = xLimit[0] + (((xLimit[1] - xLimit[0]) / divider) * multiplierX)
    decodeY = yLimit[0] + (((yLimit[1] - yLimit[0]) / divider) * multiplierY)
    return [decodeX, decodeY]

def fitnessChromosome(chromosome, xLimit, yLimit):
    decode = decodeChromosome(chromosome, xLimit, yLimit)
    fitness = (math.cos(decode[0]**2) * math.sin(decode[1]**2)) + (decode[0] + decode[1])  
    return fitness

def fitnessPopulation(population, xLimit, yLimit, totalChromosome):
    fitnessPop = []
    for i in range(totalChromosome):
        chrom = fitnessChromosome(population[i], xLimit, yLimit)
        fitnessPop.append(chrom)
    return fitnessPop

def parentSelection(population, xLimit, yLimit, totalChromosome):
    bestChromosome = []
    for _ in range(totalChromosome):
      chromosome = population[random.randint(0, totalChromosome-1)]
      if (bestChromosome == [] or fitnessChromosome(chromosome, xLimit, yLimit) > fitnessChromosome(bestChromosome, xLimit, yLimit)):
        bestChromosome = chromosome
    return bestChromosome

def crossover(parent1, parent2, probability):
    randomPC = random.random()    # untuk mencari nilai probabilitas crossover yang random
    if (randomPC < probability):    
        randomPoint = random.randint(1, 5)  # untuk mencari nilai probabilitas point yang random
        for i in range (randomPoint):
            temp = parent1[i]
            parent1[i] = parent2[i]
            parent2[i] = temp
    return [parent1, parent2]

def mutation(chromosome1, chromosome2, mutationProbability):
  probRandom = random.random()
  if probRandom < mutationProbability:
      gen1, gen2 = random.randint(0,5), random.randint(0,5)
      genValue1, genValue2 = random.randint(0,9), random.randint(0,9)
      while chromosome1[gen1] == genValue1:
        genValue1 = random.randint(0,9)
      while chromosome2[gen2] == genValue2:
        genValue2 = random.randint(0,9)
      chromosome1[gen1] = genValue1
      chromosome2[gen2] = genValue2
  return chromosome1, chromosome2

def elitism(fitnessPopulation):
  index1 = fitnessPopulation.index(max(fitnessPopulation))
  return index1

# =============================== MAIN ==================================
population = initiate_population(totalChromosome, totalGen)
fitness = fitnessPopulation(population, xLimit, yLimit, totalChromosome)
indexBest = elitism(fitness)
bestChromosome = copy.deepcopy(population[indexBest])
i = 0
bestGeneration = i
print ("Generasi     : ", i + 1)
print ("Fitness      : ", fitness[indexBest]) # menginput fitness terbaik
print ("Kromosom     : ", population[indexBest]) # menginput kromosom terbaik
print ("Dekode (X, Y): ", decodeChromosome(population[indexBest], xLimit, yLimit))
print ("================================================================================")

while i < (totalPopulation - 1):
  new_population = []
  new_population.append(population[indexBest])
  new_population.append(population[indexBest])
  while len(new_population) <= len(population): 
    parent1 = parentSelection(population, xLimit, yLimit, totalChromosome) # mencari parent 1
    parent2 = parentSelection(population, xLimit, yLimit, totalChromosome) # mencari parent 2
    while parent1 == parent2:
     parent2 = parentSelection(population, xLimit, yLimit, totalChromosome)
    offspring = crossover(parent1, parent2, probability)
    offspring = mutation(offspring[0], offspring[1], mutationProbability)
    new_population.append(offspring[0])
    new_population.append(offspring[1])
  i += 1
  fitness = fitnessPopulation(new_population, xLimit, yLimit, totalChromosome)
  indexBest = elitism(fitness)
  population = new_population

  print ("Generasi     : ", i + 1)
  print ("Fitness      : ", fitness[indexBest])
  print ("Kromosom     : ", new_population[indexBest])
  print ("Decode (X, Y): ", decodeChromosome(new_population[indexBest], xLimit, yLimit))
  print ("================================================================================")

  if fitnessChromosome(bestChromosome, xLimit, yLimit) < fitnessChromosome(new_population[indexBest], xLimit, yLimit):
    bestChromosome = copy.deepcopy(new_population[indexBest])
    bestGeneration = i

print (" ")
print ("=============================== Hasil Terbaik ==================================")
print ("Generasi     : ", bestGeneration + 1)
print ("Fitness      : ", fitnessChromosome(bestChromosome, xLimit, yLimit))
print ("Kromosom     : ", bestChromosome)
print ("Decode (X, Y): ", decodeChromosome(bestChromosome, xLimit, yLimit))