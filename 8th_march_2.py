"""
numbers = [1, 2, 3, 4, 5, 6, 7]
Expected output:

[1, 4, 9, 16, 25, 36, 49]
"""
numbers = [1, 2, 3, 4, 5, 6, 7]
numbersSquared = []
for i in range(len(numbers)):
    numbersSquared.append(numbers[i]**2)

print(numbersSquared)