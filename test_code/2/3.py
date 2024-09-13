# Given a positive integer, return the sum of all integers from 1 up to this number.

import unittest
import random


# Run test cases


def run_test_sum_of_integer(func):
    """
    Run test cases for the given function to calculate the sum of integers from 1 to n.

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

    # Helper function to handle test result
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

    # Test cases
    class TestSumOfInteger(unittest.TestCase):
        # Hidden Test Cases
        def test_hidden_cases(self):
            inputs = [random.randint(200, 800) for _ in range(70)]
            expected = [sum_of_integer(n) for n in inputs]
            results = [func(n) for n in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        # Open Test Cases
        def test_open_cases(self):
            inputs = [random.randint(100, 200) for _ in range(20)]
            expected = [sum_of_integer(n) for n in inputs]
            results = [func(n) for n in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        # Test Negative Number

        def test_negative_number(self):
            inputs = [-random.randint(100, 200) for _ in range(10)]
            expected = [None for _ in inputs]
            results = [func(n) for n in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSumOfInteger)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_sum_of_integer(
        sum_of_integer)

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
