# Given a point (x1, y1), return the quadrant in which this point lies.
# The quadrants are numbered as follows:
# 0: origin
# 1: first quadrant
# 2: second quadrant
# 3: third quadrant
# 4: fourth quadrant
# 12: positive y-axis
# 23: negative x-axis
# 34: negative y-axis
# 41: positive x-axis

import unittest
import random

# Run Test Case


def run_test_find_quadrant(func):
    """
    Runs test cases for the given function to find the quadrant of a given point X,Y.
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

    # Handles Open Test Cases
    def handle_test_result(inputs, expected, result):
        if result == expected:
            successful_inputs.append(inputs)
        else:
            failed_inputs.append(inputs)

    # Handles Hidden Test Cases
    def handle_hidden_test_result(inputs, expected, result):
        if result == expected:
            successful_hidden_inputs.append(inputs)
        else:
            failed_hidden_inputs.append(inputs)

    class TestCase(unittest.TestCase):

        # Hidden Case:
        def test_hidden_case(self):
            inputs = [(random.uniform(-100, 100), random.uniform(-100, 100))
                      for _ in range(92)]
            expected = [find_quadrant(x, y) for x, y in inputs]
            for x, y in inputs:
                result = func(x, y)
                handle_hidden_test_result(
                    (x, y), expected[inputs.index((x, y))], result)

        # Open Test Case:
        def test_quadrant_1(self):
            x, y = (random.uniform(1, 100), random.uniform(1, 100))
            result = func(x, y)
            handle_test_result((x, y), 1, result)

        def test_quadrant_2(self):
            x, y = (random.uniform(-100, -1), random.uniform(1, 100))
            result = func(x, y)
            handle_test_result((x, y), 2, result)

        def test_quadrant_3(self):
            x, y = (random.uniform(-100, -1), random.uniform(-100, -1))
            result = func(x, y)
            handle_test_result((x, y), 3, result)

        def test_quadrant_4(self):
            x, y = (random.uniform(1, 100), random.uniform(-100, -1))
            result = func(x, y)
            handle_test_result((x, y), 4, result)

        def test_pos_x_axis(self):
            x, y = (random.uniform(1, 100), 0)
            result = func(x, y)
            handle_test_result((x, y), 41, result)

        def test_neg_x_axis(self):
            x, y = (random.uniform(-100, -1), 0)
            result = func(x, y)
            handle_test_result((x, y), 23, result)

        def test_pos_y_axis(self):
            x, y = (0, random.uniform(1, 100))
            result = func(x, y)
            handle_test_result((x, y), 12, result)

        def test_neg_y_axis(self):
            x, y = (0, random.uniform(-100, -1))
            result = func(x, y)
            handle_test_result((x, y), 34, result)

    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    # Run the test suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_find_quadrant(
        find_quadrant)

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
