# Given a positive integer (n), return a list containing the first n integers in the Fibonacci series.

import unittest
import random


# Run Test Cases
def run_test_fibonacci_series(func):
    """
    Run test cases for the given function to check if it generates the correct Fibonacci series.

    Args:
        func (function): The function to test.

    Returns:
        successful_inputs (list): A list containing the successful test cases.
        failed_inputs (list): A list containing the failed test cases.
        successful_hidden_inputs (list): A list containing the successful hidden test cases.
        failed_hidden_inputs (list): A list containing the failed hidden test cases.
    """
    successful_hidden_inputs = []
    failed_hidden_inputs = []
    successful_inputs = []
    failed_inputs = []
    # Helper function to handle the test results
    def handle_hidden_test_result(inputs, expected, result):
        if result == expected:
            successful_hidden_inputs.append(inputs)
        else:
            failed_hidden_inputs.append(inputs)
        
    def handle_test_result(inputs, expected, result):
        if result == expected:
            successful_inputs.append(inputs)
        else:
            failed_inputs.append(inputs)

    # Test Cases
    class TestFibonacciList(unittest.TestCase):

        # Open Cases
        def test_open_cases(self):
            inputs = [random.randint(0,15) for _ in range(10)]
            expected = [generate_fibonacci(n) for n in inputs]
            results = [func(n) for n in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

        # Hidden Cases
        def test_hidden_cases(self):
            inputs = [random.randint(0, 200) for _ in range(90)]
            expected = [generate_fibonacci(n) for n in inputs]
            results = [func(n) for n in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        

    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFibonacciList)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return (
        successful_inputs,
        failed_inputs,
        successful_hidden_inputs,
        failed_hidden_inputs,
    )


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_fibonacci_series(generate_fibonacci)

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

    