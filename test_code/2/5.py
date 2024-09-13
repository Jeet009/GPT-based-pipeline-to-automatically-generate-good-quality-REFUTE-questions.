# Given a positive integer greater than 1, return the sum of all even numbers from 2 up to this number.

import unittest
import random


# Run Test Cases


def run_test_sum_even_numbers(func):
    """
    Run test cases for the given function to calculate the sum of even numbers up to n

    Parameters:
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

    # Helper function to handle the test result
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
    class TestSumevenNumbers(unittest.TestCase):

        # Hidden test cases:
        def test_hidden_cases(self):
            inputs = [random.randint(200, 10000) for _ in range(70)]
            expected = [sum_even_numbers(x) for x in inputs]
            results = [func(x) for x in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        # Open test cases:
        def test_open_cases(self):
            inputs = [random.randint(20, 1000) for _ in range(20)]
            expected = [sum_even_numbers(x) for x in inputs]
            results = [func(x) for x in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        # Test negative inputs

        def test_negative_number(self):
            inputs = [random.randint(-200, -99) for _ in range(10)]
            expected = [None] * 10
            results = [func(x) for x in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSumevenNumbers)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_sum_even_numbers(
        sum_even_numbers)

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
