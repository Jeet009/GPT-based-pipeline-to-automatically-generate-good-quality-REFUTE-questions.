# Given a positive integer, return the number of even digits in it.

import unittest
import random

# Run Test Cases


def run_test_even_digits_count(func):
    """
    Run test cases for the given function to calculate number of even digits in a positive integer

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

    # Helper functions to handle test result
    def handle_hidden_test_result(inputs, expected, actual):
        if expected == actual:
            successful_hidden_inputs.append(inputs)
        else:
            failed_hidden_inputs.append(inputs)

    def handle_test_result(inputs, expected, actual):
        if expected == actual:
            successful_inputs.append(inputs)
        else:
            failed_inputs.append(inputs)

    # Test Cases
    class TestEvenDigitsCount(unittest.TestCase):

        # Hidden Test Cases
        def test_hidden_cases(self):
            inputs = [random.randint(1, 9999999999) for _ in range(64)]
            expected = [count_even_digits_str(num) for num in inputs]
            results = [func(num) for num in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        def test_hidden_negative_cases(self):
            inputs = [-random.randint(1, 9999999999) for _ in range(20)]
            expected = [count_even_digits_str(num) for num in inputs]
            results = [func(num) for num in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        # Open Test Cases
        def test_open_cases(self):
            inputs = [random.randint(1, 9999999999) for _ in range(10)]
            expected = [count_even_digits_str(num) for num in inputs]
            results = [func(num) for num in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        # Open Negative Test Cases

        def test_open_negative_cases(self):
            inputs = [-random.randint(1, 9999999999) for _ in range(5)]
            expected = [count_even_digits_str(num) for num in inputs]
            results = [func(num) for num in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        # Open Zero Test Cases

        def test_open_zero_cases(self):
            inputs = [0]
            expected = [count_even_digits_str(num) for num in inputs]
            results = [func(num) for num in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEvenDigitsCount)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_even_digits_count(
        count_even_digits)

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
