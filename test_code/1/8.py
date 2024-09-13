# Given a quadratic equation with coefficients a, b and c, return the two solutions (may be real or complex).
#  You should not take the square root of a negative number in your code. Output should be a list of two tuples.
# So if the roots are 1+2j and 1–2j, the output of the function should be [(1,2), (1,-2)]. If the roots are real,
# then the second part of both the tuples becomes zero.

import unittest
import random

# Run Test Cases


def run_test_quadratic_solver(func):
    """
    Runs a test case for the quadratic_solver function.
    The test case generates random coefficients a, b and c, and checks that the function returns the correct roots.
    Args:
        func (function): The quadratic_solver function to test.
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

    # Test cases

    class TestQuadraticSolver(unittest.TestCase):

        # Hidden Test Cases:
        def test_hidden_cases(self):
            inputs = [(random.uniform(-100, 100), random.uniform(-100, 100), random.uniform(-100, 100))
                      for _ in range(90)]
            expected = [quadratic_solver(*ip) for ip in inputs]
            result = [func(*ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], result[i])

        # Open Test Cases:
        def test_open_cases(self):
            inputs = [(random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10))
                      for _ in range(10)]
            expected = [quadratic_solver(*ip) for ip in inputs]
            result = [func(*ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], result[i])

        # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQuadraticSolver)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_quadratic_solver(
        quadratic_solver)

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
