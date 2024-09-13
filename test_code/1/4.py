# Given a year, return True if it is a leap year, else return False.
# A leap year is divisible by 4, except for years that are divisible by 100. However,
# years that are divisible by 400 are also leap years.

import unittest
import random

# Run Test Cases


def run_test_leap_year(func):
    """Run test cases for Leap Year
    Args:
        func (function): The function to test.
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
        if expected == result:
            successful_inputs.append(inputs)
        else:
            failed_inputs.append(inputs)

    # Handle Hidden Test Results
    def handle_hidden_test_result(inputs, expected, result):
        if expected == result:
            successful_hidden_inputs.append(inputs)
        else:
            failed_hidden_inputs.append(inputs)

    # Test Cases
    class TestCase(unittest.TestCase):

        # Hidden Test Cases
        def test_hidden_1(self):
            inputs = [(random.randint(500, 3000)) for _ in range(10)]
            expected = [is_leap_year(year) for year in inputs]
            for i, e in zip(inputs, expected):
                result = func(i)
                handle_hidden_test_result(i, e, result)

        # Open Test Cases
        def test_not_leap_year(self):
            inputs = [1900, 2021, 1700, 2023]
            expected = [False, False, False, False]
            for i, e in zip(inputs, expected):
                result = func(i)
                handle_test_result(i, e, result)

        def test_leap_year(self):
            inputs = [2000, 2004, 2016, 2020, 2400]
            expected = [True, True, True, True, True]
            for i, e in zip(inputs, expected):
                result = func(i)
                handle_test_result(i, e, result)

        def test_zero(self):
            ip = 0
            expected = True
            result = func(ip)
            handle_test_result(ip, expected, result)

    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)

    # Run the test suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_leap_year(is_leap_year)

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
