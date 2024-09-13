# Given a list of positive integers, return a list of the factorial of all these numbers.

import unittest
import random


def run_test_factorial_list(func):
    """
    Run tests on the function to calculate the factorial of a list of positive integers.

    Args:
        func (function): The function to test.
    """
    successful_hidden_inputs = []
    failed_hidden_inputs = []
    successful_inputs = []
    failed_inputs = []

    # Helper functions to handle the test result
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

    class TestFactorialList(unittest.TestCase):
         # Hidden Test Cases
        def test_hidden_cases(self):
            inputs = [[random.randint(1, 40) for _ in range(random.randint(1,20))] for _ in range(30)]
            expected = [factorial_list(n) for n in inputs]
            results = [func(n) for n in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        # Open Test Cases
        def test_open_cases(self):
            inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            expected = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
            results = func(inputs)
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

        # Test Negative Number
        def test_negative_number(self):
            inputs = [[random.randint(-100, -1)for _ in range(random.randint(1,4))] for _ in range(4)]
            expected = [factorial_list(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        
        def test_zero_list(self):
            inputs = [[0 for _ in range(random.randint(1, 5))] for _ in range(4)]
            expected = [factorial_list(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

        def test_empty_list(self):
            inputs = []
            expected = []
            results = func(inputs)
            handle_test_result(inputs, expected, results)

             
    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFactorialList)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return (
        successful_inputs,
        failed_inputs,
        successful_hidden_inputs,
        failed_hidden_inputs,
    )


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_factorial_list(factorial_list)

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
    
