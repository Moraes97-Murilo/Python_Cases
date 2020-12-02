#data came from https://mortalidade.inca.gov.br/
#the CSV file will be at the repo

import matplotlib.pyplot as plt

data = open("Modelo01_20201202103026.csv").readlines()

x = []
y = []

for i in range(len(data)):
  if i >= 3:
    line = dados[i].split(";")
    x.append(float(line[0]))
    y.append(float(line[2]))
plt.scatter(x,y, marker='s', color='k', s='250')
plt.plot(x,y)
plt.bar(x,y)
plt.tittle("Deaths by Leukemia in Brazil(2000-2018)")
plt.xlabel("Year")
plt.ylabel("Deaths by Leukemia")
plt.show()
