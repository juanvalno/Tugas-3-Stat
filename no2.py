import statistics
import numpy as np

dataA = [100,102,99,98,101,103,104,100,98,101,100,
         99,100.102,100,105,107,106,103,100,101,102,
         105,103,102,101,100,99,98,97]

# perhitungan manualy
rataA = np.mean(dataA)

print("Rata A : " + str(rataA))

# akar panggkat 2
list_varianA = []
list_varianB = []
for index in dataA :
  list_varianA.append((index - rataA) ** 2)


# bagi total sampel
varianA = sum(list_varianA) / (len(dataA) - 1)

# akar kuadarat
simpA = statistics.sqrt(varianA)
print("Manualy")
print("Simpangan Baku A : " + str(simpA))

# munggunakan libary
smpA = statistics.stdev(dataA)
print("\nLibary")
print(smpA)
