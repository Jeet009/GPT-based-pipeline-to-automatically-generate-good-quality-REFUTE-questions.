# Given a positive integer, return the sum of all prime numbers from 1 up to this number.
import unittest
import random

# Run Test Cases

def run_test_sum_primes(func):
    """
    Run the test cases for the given function to test the sum of a primes numbers in a given range

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

    # Helper functions to handle the test results
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
    
    # Test Cases
    class TestSumPrimes(unittest.TestCase):

        # Hidden Cases
        def test_hidden_cases(self):
            inputs = [random.randint(1, 10000) for _ in range(90)]
            expected = [sum_primes(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        # Open Cases
        def test_negative_input(self):
            inputs = random.randint(-100, -1)
            expected = 0
            results = func(inputs)
            handle_test_result(inputs, expected, results)
        
        def test_zero_input(self):
            inputs = 0
            expected = 0
            results = func(inputs)
            handle_test_result(inputs, expected, results)

        def test_one_input(self):
            inputs = 1
            expected = 0
            results = func(inputs)
            handle_test_result(inputs, expected, results)
        def test_small_input(self):
            inputs = random.randint(2, 10)
            expected = sum_primes(inputs)
            results = func(inputs)
            handle_test_result(inputs, expected, results)
        
        def test_large_input(self):
            inputs = [random.randint(20,170) for _ in range(6)]
            expected = [sum_primes(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
    
    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSumPrimes)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_sum_primes(
        sum_primes)

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

