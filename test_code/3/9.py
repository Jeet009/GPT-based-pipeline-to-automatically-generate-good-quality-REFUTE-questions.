# Given a list of integers, return their Greatest Common Divisor (Divisor).

import unittest
import random
from math import gcd
from functools import reduce

# Run Test Cases
def run_test_gcd_list(func):
    """
    Run test cases for function to find GCD of a list of integers
    Args:
        func: Function to test
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
    

    # Helper Functions to handle the test result
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
    class TestGCDList(unittest.TestCase):

        # Hidden Test Cases
        def test_hidden_cases(self):
            inputs = [[random.randint(-1000,1000) for _ in range(random.randint(1,20))] for _ in range(85)]
            expected = [reduce(gcd, ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])
        

        # Open Cases
        def test_mixed_integer_open_cases(self):
            inputs = [[random.randint(-100, 100) for _ in range(random.randint(1, 7))] for _ in range(5)]
            expected = [reduce(gcd, ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

        def test_positive_integer_open_cases(self):
            inputs = [[random.randint(1, 100) for _ in range(random.randint(1, 7))] for _ in range(5)]
            expected = [reduce(gcd, ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        
        # Edge Cases
        def test_empty_list(self):
            inputs = []
            expected = 0
            result = func(inputs)
            handle_test_result(inputs, expected, result)

        def test_single_element_list(self):
            inputs = [[random.randint(-100, 100)] for _ in range(3)]
            expected = [reduce(gcd,ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        
        def test_with_zero(self):
            inputs = [0, 0, 0]
            expected = 0
            result = func(inputs)
            handle_test_result(inputs, expected, result)
            

    
    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGCDList)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return (
        successful_inputs,
        failed_inputs,
        successful_hidden_inputs,
        failed_hidden_inputs,
    )


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_gcd_list(gcd_list)

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

