# Given a temperature in Celsius, convert it to Fahrenheit using the formula F = (C * 1.8) + 32.
# Examples: If the temperature is above 90°F, Return True otherwise, Return False.

import unittest
import random

# Run Test Cases
def run_test_C_to_F(func):
    """Run test cases for Celsius to Fahrenheit Conversion
    Args:
        func (function): Function to test
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

        # Hidden Test Case
        def test_hidden_case(self):
            inputs = [random.randint(-100, 100) for _ in range(10)]
            fah = [((a*1.8)+32) for a in inputs]
            expected = [True if a > 90 else False for a in fah]
            for i, e in zip(inputs, expected):
                result = func(i)
                handle_hidden_test_result(i, e, result)

        # Open Test Case
        def test_open_case(self):
            inputs = [42, 35, 40, 20, -10, 0, 17.77777777777778]
            expected = [True, True, True, False, False, False, False]
            for i, e in zip(inputs, expected):
                result = func(i)
                handle_test_result(i, e, result)

    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)

    # Run the test suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_C_to_F(
        celsius_to_fahrenheit)

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
