def radix_sort(list):
    """
    --------------------------------------------------------
    This function sorts a list of primes using radix sort.
    --------------------------------------------------------
    Parameters:
        list - a list of prime numbers
    Returns:
        list = the new sorted list
    """
    # Create a list of empty lists
    buckets = [[] for i in range(10)]

    # Find the max prime number in the list
    max_prime = max(list)

    # Find the number of digits in the max prime number
    max_digit = len(str(max_prime))

    # Iterate through the number of digits in the max prime number
    for digit in range(max_digit):
        # Iterate through the list
        for num in list:
            # Find the digit in the prime number
            digit_value = (num // 10 ** digit) % 10
            # Add the prime number to the right bucket
            buckets[digit_value].append(num)
        # Clear the list of primes
        list.clear()
        # Iterate through the buckets
        for bucket in buckets:
            # Add the primes in the bucket to the list of primes
            list.extend(bucket)
            # Clear the bucket
            bucket.clear()

    return list



