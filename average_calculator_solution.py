def calculate_average(numbers):
    if not numbers:
        return 0
    for number in numbers:
        if not isinstance(number,(int, float)):
            raise TypeError("List elements must be numeric.")
    return sum(numbers) / len(numbers)