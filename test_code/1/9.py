# Given three points, return True if they lie on the same straight line, else return False.

import unittest
import random

# Test Cases
def run_test_collinear(func):
    """
    Run test cases for collinear function
    Args:
        func: collinear function to test
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

    # Helper function to Handle the the test results
    def handle_test_result(inputs, expected, result):
        if expected == result:
            successful_inputs.append(inputs)
        else:
            failed_inputs.append(inputs)

    def handle_hidden_test_result(inputs, expected, result):
        if expected == result:
            successful_hidden_inputs.append(inputs)
        else:
            failed_hidden_inputs.append(inputs)

    class TestCollinear(unittest.TestCase):

        # Hidden Test Cases
        def test_hidden_cases(self):
            inputs = [(random.uniform(-1000, 1000), random.uniform(-1000, 1000), random.uniform(-1000, 1000),
                       random.uniform(-1000, 1000), random.uniform(-1000, 1000), random.uniform(-1000, 1000)) for _ in range(90)]
            expected = [on_same_line(*ip) for ip in inputs]
            result = [func(*ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], result[i])

        # Open test cases
        def test_open_cases(self):
            inputs = [(random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100),
                       random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)) for _ in range(10)]
            expected = [on_same_line(*ip) for ip in inputs]
            result = [func(*ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], result[i])

       # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCollinear)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_collinear(
        on_same_line)

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
