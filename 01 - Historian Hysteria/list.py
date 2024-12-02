array1 = []
array2 = []
result = 0
with open("input\input01.txt", "r") as file:
    for line in file:
        numbers = line.split()  
        array1.append(int(numbers[0]))  
        array2.append(int(numbers[1])) 
array1.sort()
array2.sort()

# PART 1 result between each index
# for i in range(len(array1)):
#     result += abs(array1[i] - array2[i])

# print(result)

# PART 2 similarity scores
for i in range(len(array1)):
    low, high = 0, len(array2) - 1
    while low <= high:
        mid = (low + high) // 2
        if array2[mid] < array1[i]:
            low = mid + 1
        else:
            high = mid - 1

    # Count occurrences of array1[i] in array2
    count = 0
    while low < len(array2) and array2[low] == array1[i]:
        count += 1
        low += 1

    # Multiply the value at i (array1) with the amount of occurrences and add to result
    result += array1[i] * count

print(result)
    