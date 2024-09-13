# Given a list of numbers, return another list of co-primes and count how many co-primes are there in this given list.

import unittest
import random

# Run Test Cases
def run_test_coprime_list(func):
    """
    Run tests on the function to check if it returns the correct output for different inputs for finding co-primes from a list and their count 
    Args:
        func (function): The coprime_list function to test
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
    def handle_hidden_test_result(inputs, expected, results):
        if results == expected:
            successful_hidden_inputs.append(inputs)
        else:
            failed_hidden_inputs.append(inputs)
    
    def handle_test_result(inputs, expected, results):
        if results == expected:
            successful_inputs.append(inputs)
        else:
            failed_inputs.append(inputs)

    class TestCoprimeList(unittest.TestCase):
        # Hidden Cases
        def test_hidden_cases(self):
            inputs = [[random.randint(1, 100) for _ in range(random.randint(1, 40))]for _ in range(90)]
            expected = [coprime_list(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        # Open Cases
        def test_empty_list(self):
            inputs = []
            expected = ([], 0)
            results = func(inputs)
            handle_test_result(inputs, expected, results)

        def test_single_element_list(self):
            inputs = [random.randint(1, 100)]
            expected = ([], 0)
            results = func(inputs)
            handle_test_result(inputs, expected, results)
        
        def test_two_element_list(self):
            inputs = [[random.randint(1, 100), random.randint(1, 100)]for _ in range(3)]
            expected = [coprime_list(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

        def test_custom_known_list(self):
            inputs = [4, 6, 9, 10]
            expected = ([[4, 9], [9, 10]], 2)
            results = func(inputs)
            handle_test_result(inputs, expected, results)
        
        def test_large_list(self):
            inputs = [[random.randint(1, 100) for _ in range(10)]for _ in range(4)]
            expected = [coprime_list(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCoprimeList)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_coprime_list(
        coprime_list)

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




