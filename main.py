"""
CISC-121 2023W
Name:   Ethan Nguyen
Student Number: 20235183
Email:  20hen@queensu.ca
Date: 2023-03-15

I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
"""

import functions

import a4_q2


def main():
    """
    This function takes two strings as input and checks if they are anagrams.
    """
    # Get user input
    string1 = input("Enter a string: ")
    string2 = input("Enter another string: ")

    # Check if the strings are uppercase
    if string1.isupper() == True and string2.isupper() == True:

        # Check if the strings contain spaces
        if " " in string1 or " " in string2:
            print("You're not allowed to use spaces")

        # Check if the strings are of type string
        elif not isinstance(string1, str) or not isinstance(string2, str):
            print("You can only input strings")

        # Check if strings are anagrams if conditions satisfied
        else:
            # Iterate through the strings and map characters to prime numbers
            prime1 = [functions.char_prime(char) for char in string1]
            prime2 = [functions.char_prime(char) for char in string2]

            # Print list of primes corresponding to the given strings
            print("Primes for string1:", prime1)
            print("Primes for string2:", prime2)

            # Sort list of primes using radix sort
            sorted_prime_1 = a4_q2.radix_sort(prime1)
            sorted_prime_2 = a4_q2.radix_sort(prime2)

            # Print list of sorted primes
            print("Sorted primes for string1:", sorted_prime_1)
            print("Sorted primes for string1:", sorted_prime_2)
            anagram = functions.is_anagram(string1, string2)

            # Check whether string are anagrams
            if anagram == True:
                print("The strings are anagrams")
            else:
                print("The strings are not anagrams")

    else:
        print("Your string has to be all uppercase")


main()
