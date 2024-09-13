# Given a list of numbers, return their mean and standard deviation.

# Return the result upto 5 decimal places. using round(value, 5) function

import unittest
import random
import statistics
import math

# Run Test cases
def run_test_mean_std_dev(func):
    """
    Run test cases for the given function to calculate mean and standard deviation.

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
    class TestMeanStd(unittest.TestCase):

        # Hidden Cases
        def test_hidden_mixed_integer_cases(self):
            inputs = [[random.randint(-10000, 10000) for _ in range(random.randint(1,20))] for _ in range(45)]
            expected = [(round(statistics.mean(ip),5), round(statistics.stdev(ip), 5) if len(ip) > 1 else 0) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        # To be checked
        def test_hidden_mixed_float_cases(self):
            inputs = [[random.uniform(-100, 100) for _ in range(random.randint(1, 20))] for _ in range(45)]
            expected = [(round(statistics.mean(ip),5), round(statistics.stdev(ip),5) if len(ip) > 1 else 0) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        # Open Test Cases
        def test_open_mixed_integer_cases(self):
            random.seed(32)
            inputs = [[random.randint(-10000, 10000) for _ in range(random.randint(1,7))] for _ in range(5)]
            expected = [(round(statistics.mean(ip),5), round(statistics.stdev(ip),5) if len(ip) > 1 else 0) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

        def test_open_mixed_float_cases(self):
            random.seed(32)
            inputs = [[random.uniform(-100, 100) for _ in range(random.randint(1, 7))] for _ in range(5)]
            expected = [(round(statistics.mean(ip), 5), round(statistics.stdev(ip), 5) if len(ip) > 1 else 0) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMeanStd)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_mean_std_dev(
        mean_std)

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