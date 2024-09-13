# Given a list of integers, return their Least Common Multiple (LCM).

import unittest
import random
import math
from functools import reduce


def run_test_lcm_list(func):
    """
    Run test cases for function to check LCM of a lsit of integer
    Args:
    func (function): The find_index function to test.

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
    # Helper function to find GCD of two numbers
    def gcd(a, b):
        a, b = abs(a), abs(b)
        while b:
            a, b = b, a % b
        return a

    lcm_list = lambda nums: reduce(lambda a, b: abs(a * b) // math.gcd(a, b), nums) if nums else 0

    # Helper Functions to handle the test results
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
    class TestLCMList(unittest.TestCase):

        # Hidden Cases
        def test_hidden_case_1(self):
            inputs = [[random.randint(-1000,1000) for _ in range(random.randint(1,20))] for _ in range(85)]
            expected = [lcm_list(nums) for nums in inputs]
            result = [func(nums) for nums in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], result[i])

        
        # Open Cases
        def test_mixed_integer_open_cases(self):
            inputs = [[random.randint(-100,100) for _ in range(random.randint(1,7))] for _ in range(5)]
            expected = [lcm_list(nums) for nums in inputs]
            results = [func(nums) for nums in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

        def test_positive_integer_open_cases(self):
            inputs = [[random.randint(1, 100) for _ in range(random.randint(1, 7))] for _ in range(5)]
            expected = [lcm_list(nums) for nums in inputs]
            results = [func(nums) for nums in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

        # Edge Cases
        def test_single_element(self):
            inputs = [[random.randint(-100, 100)] for _ in range(4)]
            expected = [lcm_list(ip) for ip in inputs]
            result = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], result[i])
        def test_empty_list(self):
            inputs = [] 
            expected = 0
            result = func(inputs)
            handle_test_result(inputs, expected, result)
        

    

    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLCMList)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return (
        successful_inputs,
        failed_inputs,
        successful_hidden_inputs,
        failed_hidden_inputs,
    )


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_lcm_list(lcm_list_i)

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

    
