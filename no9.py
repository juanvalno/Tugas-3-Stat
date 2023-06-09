import statistics
import numpy as np

dataA = [20,25,22,18,23]
dataB = [28,30,26,24,27]

# perhitungan manualy
rataA = np.mean(dataA)
rataB = np.mean(dataB)

print("Rata A : " + str(rataA))
print("Rata B : " + str(rataB))

# akar panggkat 2
list_varianA = []
list_varianB = []
for index in dataA :
  list_varianA.append((index - rataA) ** 2)
  
for index in dataA :
  list_varianB.append((index - rataB) ** 2)

# bagi total sampel
varianA = sum(list_varianA) / (len(dataA) - 1)
varianB = sum(list_varianB) / (len(dataB) - 1)

# akar kuadarat
simpA = statistics.sqrt(varianA)
simpB = statistics.sqrt(varianB)
print("Manualy")
print("Simpangan Baku A : " + str(simpA))
print("Simpangan Baku B : " + str(simpB))

# munggunakan libary
smpA = statistics.stdev(dataA)
smpB = statistics.stdev(dataB)
print("\nLibary")
print(smpA)
print(smpB)
