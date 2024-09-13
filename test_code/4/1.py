# Given a list of distinct numbers, return another list which contains the sum of all pairs of numbers in the given list
# (the same pair should not be taken twice).

import unittest
import random

# Run Test Cases
def run_test_pair_sum(func):
    """
    Runs the test cases for the given function to check sum of all pairs in a list of numbers in the given input list

    Args:
        func (function): The function to test.

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
    def handle_hidden_test_result(inputs, expected,result):
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
    class TestSumPairs(unittest.TestCase):

        # Open Cases
        def test_empty_list(self):
            inputs = []
            expected = []
            result = func(inputs)
            handle_test_result(inputs, expected, result)
        
        def test_single_element_list(self):
            inputs = [random.randint(-100,100)] 
            expected = []
            results = func(inputs)
            handle_test_result(inputs, expected, results)
        def test_two_element_list(self):
            inputs = [[random.randint(-100, 100), random.randint(-100, 100)]for _ in range(2)]
            expected = [sum_pairs(ip) for ip in inputs]
            results = [func(ip) for  ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        def test_large_list(self):
            inputs = [[random.randint(-100, 100) for _ in range(random.randint(1, 7))] for _ in range(5)]
            expected = [sum_pairs(ip) for ip in inputs]
            results = [func(ip) for  ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

        def test_duplicate_numbers(self):
            inputs = [2,3,3,4]
            expected = [5,6,7]
            results = func(inputs)
            handle_test_result(inputs, expected, results)

        # Hidden Cases
        def test_hidden_int_cases(self):
            # If you take more numbers of elements in the list it will take more time to compute the sum pairs list
            # So limiting to 50 elements in the list
            inputs = [[random.randint(-1000, 1000) for _ in range(random.randint(1, 50))] for _ in range(80)]
            expected = [sum_pairs(ip) for ip in inputs]
            results = [func(ip) for  ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])
        def test_hidden_float_cases(self):
            inputs = [[random.uniform(-1000, 1000) for _ in range(random.randint(1, 50))] for _ in range(10)]
            expected = [sum_pairs(ip) for ip in inputs]
            results = [func(ip) for  ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        
    

    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSumPairs)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return (
        successful_inputs,
        failed_inputs,
        successful_hidden_inputs,
        failed_hidden_inputs,
    )


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_pair_sum(sum_pairs)

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
