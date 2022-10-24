import numpy as np
import math

t1 = int(input("Input the first term: "))
t2 = int(input("Input the second term: "))
t3 = int(input("Input the third term: "))
first1 = t2 - t1
first2 = t3 - t2

second1 = first2 - first1

coefficient_a = second1 / 2

nsquared = [1, 4, 9]
sequence = [t1, t2, t3]

result = [nsquared *  coefficient_a for nsquared in nsquared]
array1 = np.array(result)
array2 = np.array(sequence)
subtracted_array = np.subtract(array2, array1)
subtracted = list(subtracted_array)

coefficient_b = subtracted[2] - subtracted[1]

coefficient_c = subtracted[0] - coefficient_b

if coefficient_c > 0:
    print(str(coefficient_a) + "x^2 " + str(coefficient_b) + "x + " + str(coefficient_c))
elif coefficient_c < 0:
    print(str(coefficient_a) + "x^2 " + str(coefficient_b) + "x " + str(coefficient_c))

finder = input("Do you want to find a term in the sequence? Type 'Y' for yes or 'N' for no: ")

while finder != "N":
    term = int(input("Which term do you want to find: "))
    y = (coefficient_a * (term**2)) + (coefficient_b * term) + (coefficient_c)
    print(y)
    finder = input("Do you want to find another term in the sequence? Type 'Y' for yes or 'N' for no: ")
