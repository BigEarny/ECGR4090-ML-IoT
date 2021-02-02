#!/usr/bin/env python
import person
import numpy as np
import matplotlib.pyplot as plt

list_of_names = ['Roger', 'Mary', 'Luisa', 'Elvis']
list_of_ages  = [23, 24, 19, 86]
list_of_heights_cm = [175, 162, 178, 182]

for name in list_of_names:
  print("The name {:} is {:} letters long".format(name, len(name)))
print("\n")

list_of_length = [len(name) for name in list_of_names]

people = {}
for name in list_of_names:
    new_person = person.person(name=name, age=list_of_ages[list_of_names.index(name)], height=list_of_heights_cm[list_of_names.index(name)])
    people.update({name:new_person.__repr__()})

print(f"The dictionary of people is shown below: \n {people}\n")

ages = np.array(list_of_ages)
heights = np.array(list_of_heights_cm)

avg_age = np.mean(ages)
print(f"The average age is {avg_age}.\n")

plt.scatter(list_of_ages, list_of_heights_cm)
plt.xlabel('Ages (year)')
plt.ylabel('Heights (cm)')
plt.title('Scatter Plot of Ages vs Heights')
plt.savefig("ScatterPlotAgeVsHeight.png")
plt.show()