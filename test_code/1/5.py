# Given two numbers, a and b, return the value of a/b (b may be zero).

import unittest
import random

# Run Test cases

def run_test_division(func):
    """Test division function with random inputs
    Args:
        func (function): The function to test
    Returns:
        tuple: (successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs)
        successful_inputs: List of tuples containing the successful inputs
        failed_inputs: List of tuples containing the failed inputs
        successful_hidden_inputs: List of tuples containing the successful hidden inputs
        failed_hidden_inputs: List of tuples containing the failed hidden inputs
    """
    successful_inputs = []
    failed_inputs = []
    successful_hidden_inputs = []
    failed_hidden_inputs = []

    # Handle Open Test Cases
    def handle_test_result(inputs, expected, result):
        if result == expected:
            successful_inputs.append(inputs)
        else:
            failed_inputs.append(inputs)

    # Handle Hidden Test Cases
    def handle_hidden_test_result(inputs, expected, result):
        if result == expected:
            successful_hidden_inputs.append(inputs)
        else:
            failed_hidden_inputs.append(inputs)

    class TestDivision(unittest.TestCase):

        # Hidden Test Cases
        def test_hidden_cases(self):
            inputs = [(random.randint(-1000, 1000), random.randint(-1000, 1000))
                      for _ in range(89)]
            expected = [(a/b) for a, b in inputs]
            for a, b in inputs:
                result = func(a, b)
                handle_hidden_test_result(
                    (a, b), expected[inputs.index((a, b))], result)

        # Open Test Cases:
        def test_zero(self):
            inputs = [(random.randint(-1000, 1000), 0)]
            expected = None
            for a, b in inputs:
                result = func(a, b)
                handle_test_result((a, b), expected, result)

        def test_normal_case(self):
            inputs = [(random.randint(-5000, 5000), random.randint(-5000, 5000))
                      for _ in range(10)]
            expected = [division(a, b) for a, b in inputs]
            for a, b in inputs:
                result = func(a, b)
                handle_test_result(
                    (a, b), expected[inputs.index((a, b))], result)

      # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDivision)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_division(division)

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
