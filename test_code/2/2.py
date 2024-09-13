# Given a positive integer, return True if it’s prime, else return False.

import unittest
import random

# Run Test Cases


def run_test_prime(func):
    """
    Run test cases for the given function to check if it correctly identifies prime numbers.

    Args:
        func (function): The function to test

    Returns:
        tuple: (successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs)
        successful_inputs: List of tuples containing the successful inputs
        failed_inputs: List of tuples containing the failed inputs
        successful_hidden_inputs: List of tuples containing the successful hidden inputs
        failed_hidden_inputs: List of tuples containing the failed hidden inputs
    """
    successful_hidden_inputs = []
    failed_hidden_inputs = []
    successful_inputs = []
    failed_inputs = []

    # Helper function to handle the test result
    def handle_hidden_test_result(inputs, expected, result):
        if result == expected:
            successful_hidden_inputs.append(inputs)
        else:
            failed_hidden_inputs.append(inputs)

    def handle_test_result(inputs, expected, result):
        if result == expected:
            successful_inputs.append(inputs)
        else:
            failed_inputs.append(inputs)

    # Sieve of eratosthenes to generate prime numbers
    def sieve_of_eratosthenes(range_int):
        """
        Generate a list of prime numbers up to the given range using the Sieve of Eratosthenes algorithm.

        Parameters:
        range_int (int): The upper limit of the range to generate primes

        Returns:
        primes (list): A list of prime numbers up to the given range
        """
        if range_int <= 1:
            return []

        primes = []
        is_prime = [True] * (range_int + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

        for num in range(2, int(range_int ** 0.5) + 1):
            if is_prime[num]:
                primes.append(num)
                for i in range(num * 2, range_int + 1, num):  # Mark multiples of the prime number as non-prime
                    is_prime[i] = False

        # Add the remaining prime numbers to the list
        for num in range(int(range_int ** 0.5) + 1, range_int + 1):
            if is_prime[num]:
                primes.append(num)

        return primes

    # Test cases
    class TestPrime(unittest.TestCase):

        # Check true primes
        def test_true_primes(self):
            primes = sieve_of_eratosthenes(1000000)
            inputs = [random.choice(primes) for _ in range(30)]
            expected = [True] * 30
            results = [func(num) for num in inputs]
            for i in range(30):
                handle_test_result(inputs[i], expected[i], results[i])

        # Hidden Test Cases:
        def test_hidden_cases(self):
            inputs = [random.randint(100, 20000) for _ in range(60)]
            expected = [is_prime(num) for num in inputs]
            results = [func(num) for num in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        # Open Test Case
        def test_open_cases(self):
            inputs = [random.randint(1000, 1000000) for _ in range(10)]
            expected = [is_prime(num) for num in inputs]
            results = [func(num) for num in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPrime)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_prime(
        is_prime)

    # Print Open Test Results
    print("Open Test Results:")
    print("TestCase Inputs:", successful_inputs)
    print("Failed Inputs:", failed_inputs)

    # Print Total Test Results
    print("Total Test Results:")
    print("Successful Inputs:", len(successful_inputs) + len(_))

    # Print Summary
    if len(failed_inputs) + len(__) == 0:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")
