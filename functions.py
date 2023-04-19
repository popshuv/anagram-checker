def char_prime(my_char):
    """
    ---------------------------------------------------------------------------------------------
    This function will map each letter to a unique prime number by writing a function that takes
    a single character and outputs the unique prime that you assign to that character
    ---------------------------------------------------------------------------------------------
    Parameters:
        my_char - a char in ABCDEFGHIJKLMNOPQRSTUVWXYZ
    Returns:
        prime_int = a prime number unique to the letter
    ---------------------------------------------------------------------------------------------
    """
    # Create a dictionary of letters and their corresponding prime numbers
    primes = {'A': 2, 'B': 3, 'C': 5, 'D': 7, 'E': 11, 'F': 13, 'G': 17,
              'H': 19, 'I': 23, 'J': 29, 'K': 31, 'L': 37, 'M': 41,
              'N': 43, 'O': 47, 'P': 53, 'Q': 59, 'R': 61, 'S': 67,
              'T': 71, 'U': 73, 'V': 79, 'W': 83, 'X': 89, 'Y': 97, 'Z': 101}
    # Return the prime number corresponding to the character
    prime_int = primes.get(my_char.upper())
    return prime_int


def primeify(my_string):
    """
    ----------------------------------------------------------------------------------------------
    This recursive function will compute the product of the character primes for a given string
    ----------------------------------------------------------------------------------------------
    Parameters:
        my_string - any string (str)
    Returns:
        prime_product = the product of all primes for each letter
    ----------------------------------------------------------------------------------------------
    """
    # Base case
    if not my_string:
        return 1
    # Recursive case
    else:
        first_char = my_string[0]
        rest_chars = my_string[1:]
        prime_product = char_prime(first_char) * primeify(rest_chars)
        return prime_product


def is_anagram(string1, string2):
    """
    ---------------------------------------------------------------------------
    This function will determine if two strings are anagrams of each other
    ---------------------------------------------------------------------------
    Parameters:
        string1, string2 - any two strings (str)
    Returns:
        Boolean variable
    ---------------------------------------------------------------------------
    """
    # Compare the products of the primes for each string
    if primeify(string1) == primeify(string2):
        return True
    else:
        return False
