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

subtracted = list()
for item1, item2 in zip(sequence, result):
    item = item1 - item2
    subtracted.append(item)

coefficient_b = subtracted[2] - subtracted[1]

coefficient_c = subtracted[0] - coefficient_b

if coefficient_a == float:
    result = result
elif coefficient_a == 1:
    result = "n^2 "
elif coefficient_a == 0:
    result = " "

if coefficient_b > 0:
    result = str(result) + " + " + str(coefficient_b) + "n"
elif coefficient_b == 0:
    result = str(result)
elif coefficient_b < 0:
    result = str(result) + " - " + str(coefficient_b)[1:] + "n"

if coefficient_c > 0:
    result = str(result) + " + " + str(coefficient_c)
elif coefficient_c == 0:
    result = str(result)
elif coefficient_c < 0:
    result = str(result) + " - " + str(coefficient_c)[1:]

print(result)

term = int(input("Input a term of the sequence you would like to find, type any non-integer value to end the program: "))

while term != int:
    y = (coefficient_a * (int(term)**2)) + (coefficient_b * int(term)) + (coefficient_c)
    print(y)
    term = input("Input a term of the sequence you would like to find, type any non-integer value to end the program: ")
