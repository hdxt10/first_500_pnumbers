def is_prime(num):
    """
    Checks if a given number is prime.

    Args:
        num: An integer to be checked for primality.

    Returns:
        True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # If divisible by any number, it's not prime
    return True  # If no divisors found, it's prime

def find_first_n_primes(n):
    """
    Finds and returns a list of the first 'n' prime numbers.

    Args:
        n: The number of prime numbers to find.

    Returns:
        A list containing the first 'n' prime numbers.
    """
    primes = []
    num = 2  # Start checking from the first prime number
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Find the first 500 prime numbers
first_500_primes = find_first_n_primes(500)

# Print the found prime numbers
print("The first 500 prime numbers are:")
print(first_500_primes)