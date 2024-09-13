# Given two points (x1, y1) and (x2, y2), return the slope and intercept of the line joining these two points
#  (the line may be perfectly horizontal or vertical).

import unittest
import random

# Run Test cases


def run_test_slope_intercept(func):
    """
        Runs the test cases for the given function to calculate Slope & Intercept
        Args:
            func (function): The slope_intercept() function to test
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

    # Handle Open Test Results
    def handle_test_result(inputs, expected, result):
        if result == expected:
            successful_inputs.append(inputs)
        else:
            failed_inputs.append(inputs)
    # Handle Hidden Test Results

    def handle_hidden_test_result(inputs, expected, result):
        if result == expected:
            successful_hidden_inputs.append(inputs)
        else:
            failed_hidden_inputs.append(inputs)

    # Test Cases
    class TestCase(unittest.TestCase):

        # Hidden Test Cases
        def test_hidden_cases(self):
            inputs = [
                (random.uniform(-100000, 100000), random.uniform(-100000, 100000),
                 random.uniform(-100000, 100000), random.uniform(-100000, 100000))
                for _ in range(95)

            ]
            expected = [slope_intercept(*ip) for ip in inputs]
            actual = [func(*ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], actual[i])

        # Open Test Cases
        def test_open_cases(self):
            inputs = [
                (random.randint(-100, 100), random.randint(-100, 100),
                 random.randint(-100, 100), random.randint(-100, 100))
                for _ in range(5)

            ]
            expected = [slope_intercept(*ip) for ip in inputs]
            actual = [func(*ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], actual[i])

       # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_slope_intercept(
        slope_intercept)

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
