# Given a list of numbers, return the maximum number in it.

import unittest
import random

# Test cases
def run_test_max_of_list(func):
    """
    Run test cases for the given function to find the maximum number in a list.

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
    class TestMaxOfList(unittest.TestCase):

        # Hidden Test Cases
        def test_hidden_integer_cases(self):
            inputs = [[random.randint(-100000,100000) for _ in range(random.randint(1,20))] for _ in range(55)]
            expected = [max(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        def test_hidden_float_cases(self):
            inputs = [[random.uniform(-100000, 100000) for _ in range(random.randint(1, 20))] for _ in range(35)]
            expected = [max(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])


        # Open Test Cases
        def test_integer_cases(self):
            inputs = [[random.randint(-100000, 100000) for _ in range(random.randint(1,7))] for _ in range(5)]
            expected = [max(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

        def test_empty_list(self):
            inputs = []
            expected = None
            result = func(inputs)
            handle_test_result(inputs, expected, result)
        
        def test_list_of_zeros(self):
            inputs = [[0] * random.randint(1, 7) for _ in range(4)]
            expected = [max(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMaxOfList)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return (
        successful_inputs,
        failed_inputs,
        successful_hidden_inputs,
        failed_hidden_inputs,
    )


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_max_of_list(find_max)

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
