# Given two integers, find the larger one.

import unittest
import random



# Run Test Cases


def run_test_find_larger(func):
    """
    Test cases for find_larger function.
    Args:
        func (function): The find_larger function to test.
    Returns:
        tuple: (successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs)
        successful_inputs: List of tuples containing the successful inputs
        failed_inputs: List of tuples containing the failed inputs
        successful_hidden_inputs: List of tuples containing the successful hidden inputs
        failed_hidden_inputs: List of tuples containing the failed hidden inputs
    """
    # List for storing test results
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
    def handle_hidden_test_result(input, expected, result):
        if result == expected:
            successful_hidden_inputs.append(input)
        else:
            failed_hidden_inputs.append(input)

    # Test Cases
    class TestCase(unittest.TestCase):

        # Hidden Test Cases
        def test_hidden_case(self):
            inputs = [
                (random.randint(-1000, 1000), random.randint(-1000, 1000))
                for _ in range(95)
            ]
            expected = [max(a, b) for a, b in inputs]
            for a, b in inputs:
                result = func(a, b)
                handle_hidden_test_result(
                    (a, b), expected[inputs.index((a, b))], result
                )

        # Open Test Cases
        def test_case_1(self):
            handle_test_result((1, 2), 2, func(1, 2))

        def test_case_2(self):
            handle_test_result((2, 1), 2, func(2, 1))

        def test_case_3(self):
            handle_test_result((0, 0), 0, func(0, 0))

        def test_case_4(self):
            handle_test_result((-1, -2), -1, func(-1, -2))

        def test_case_5(self):
            handle_test_result((-2, -1), -1, func(-2, -1))

    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return (
        successful_inputs,
        failed_inputs,
        successful_hidden_inputs,
        failed_hidden_inputs,
    )


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_find_larger(find_larger)

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
