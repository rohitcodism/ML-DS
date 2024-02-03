def mean(numbers):
    """
    Calculate the mean (average) of a list of numbers.
    """
    return sum(numbers) / len(numbers)


def median(numbers):
    """
    Calculate the median of a list of numbers.
    """
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]


def main():
    # Example data
    data = [1,6,7,4,2]

    # Calculate mean and median
    mean_value = mean(data)
    median_value = median(data)

    # Print results
    print("Data:", data)
    print("Mean:", mean_value)
    print("Median:", median_value)


if __name__ == "__main__":
    main()
