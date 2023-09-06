def subtract_average_plus_50(numbers):
    result = numbers.copy()
    length = len(numbers)

    for i in range(3, length - 3):
        average = (numbers[i - 3] + numbers[i - 2] + numbers[i - 1] + numbers[i + 1] + numbers[i + 2] + numbers[i + 3]) / 6
        difference = numbers[i] - average
        if difference >= 50:
            result[i] = min(numbers[i - 3:i + 3])

    return result

numbers = []
modified_numbers = subtract_average_plus_50(numbers)
print(modified_numbers)