# Problem 1: Given an integer, check if it is even or odd.

import unittest
import random

# Run Test Cases

def run_even_odd_test(func):
    """
    Runs the test cases for the given function for ODD-EVEN number checking.
    Args:
        func (function): The function to test.
    Returns:
        tuple: (successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs)
        successful_inputs: List of tuples containing the successful inputs
        failed_inputs: List of tuples containing the failed inputs
        successful_hidden_inputs: List of tuples containing the successful hidden inputs
        failed_hidden_inputs: List of tuples containing the failed hidden inputs
    """
    # Lists for  storing test results
    successful_inputs = []
    failed_inputs = []
    successful_hidden_inputs = []
    failed_hidden_inputs = []

    # Handle the inputs to be shown
    def handle_test_result(num, expected_result, test_result):
        if test_result == expected_result:
            successful_inputs.append(num)
        else:
            failed_inputs.append(num)

    # Handle the inputs to be hidden
    def handle_hidden_test_result(num, expected_result, test_result):
        if test_result == expected_result:
            successful_hidden_inputs.append(num)
        else:
            failed_hidden_inputs.append(num)

    # Test cases
    class TestEvenOdd(unittest.TestCase):

        # Open input TestCases
        # For positive even numbers
        def test_even_num(self):
            inputs = [
                2,
                4,
                6,
                8,
            ]  # Intentionally put 11 to check it's correctly capturing failed_inputs
            for num in inputs:
                handle_test_result(num, True, func(num))

        # For positive odd numbers
        def test_odd_num(self):
            inputs = [3, 5, 7, 9]
            for num in inputs:
                handle_test_result(num, False, func(num))

        # Testing 0 to be even or not
        def test_zero(self):
            handle_test_result(0, True, func(0))

        # For Negative even numbers
        def test_negative_even_num(self):
            inputs = [-2, -4, -6, -8, -10]
            for num in inputs:
                handle_test_result(num, True, func(num))

        # For Negative odd numbers
        def test_negative_odd_num(self):
            inputs = [-3, -5, -7, -9]
            for num in inputs:
                handle_test_result(num, False, func(num))

        # Hidden Input TestCases

        # For positive even numbers
        def test_hidden_even_num(self):
            # Generates 10 random positive even numbers
            numbers = [num for num in range(200, 999) if num % 2 == 0]
            inputs = random.sample(numbers, 41)
            for num in inputs:
                handle_hidden_test_result(num, True, func(num))

        # For positive odd numbers
        def test_hidden_odd_num(self):
            # Generates 10 random positive odd numbers
            numbers = [num for num in range(200, 999) if num % 2 != 0]
            inputs = random.sample(numbers, 41)
            for num in inputs:
                handle_hidden_test_result(num, False, func(num))

    # Create a test suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEvenOdd)
    # Run the test suite
    final = unittest.TextTestRunner().run(suite)

    # Return the test results
    return (
        successful_inputs,
        failed_inputs,
        successful_hidden_inputs,
        failed_hidden_inputs,
    )


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_even_odd_test(is_even)
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
