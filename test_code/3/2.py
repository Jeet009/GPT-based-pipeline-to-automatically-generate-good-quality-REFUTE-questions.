# Given a list of numbers, return a list of the squares of all the numbers.

import unittest
import random


# Run Test Cases
def run_test_squared_list(func):
    """
    Run test cases for the function to calculate the squares of numbers in a list.

    Args:
        func (function): The square_list function to test
    
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
    class TestSquaredList(unittest.TestCase):

        # Hidden Test Cases
        def test_hidden_positive_int_cases(self):
            inputs = [[random.randint(1,10000) for _ in range(random.randint(1,20))] for _ in range(30)]
            expected = [[num ** 2 for num in nums] for nums in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])
        def test_hidden_mixed_integer(self):
            inputs = [[random.randint(-10000, 10000) for _ in range(random.randint(1,20))] for _ in range(30)]
            expected = [[num ** 2 for num in nums] for nums in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])
        def test_hidden_mixed_float(self):
            inputs = [[random.uniform(-10000, 10000) for _ in range(random.randint(1,20))] for _ in range(30)]
            expected = [[num ** 2 for num in nums] for nums in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        # Open Test Cases
        def test_positive_cases(self):
            inputs = [[random.randint(1,100000) for _ in range(random.randint(1,5))] for _ in range(3)]
            expected = [[num ** 2 for num in nums] for nums in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        
        def test_mixed_cases(self):
            inputs = [[random.randint(-10000, 10000) for _ in range(random.randint(1,5))] for _ in range(3)]
            expected = [[num ** 2 for num in nums] for nums in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        def test_float_mixed_cases(self):
            inputs = [[random.uniform(-10000, 10000) for _ in range(random.randint(1, 5))] for _ in range(2)]
            expected = [[num ** 2 for num in nums] for nums in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        # Test not a list
        def test_not_a_list(self):
            inputs = "not a  list"
            expected = None
            results = func(inputs)
            handle_test_result(inputs, expected, results)
        # Test empty list
        def test_empty_list(self):
            inputs = []
            expected = []
            results = func(inputs)
            handle_test_result(inputs, expected, results)

    

    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSquaredList)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_squared_list(
        square_list)

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