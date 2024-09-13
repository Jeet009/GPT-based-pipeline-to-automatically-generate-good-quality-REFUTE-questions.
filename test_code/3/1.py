# Given a list of numbers, return its length and the sum of all these numbers.

import unittest
import random

# Run Test cases
def run_test_cases_sum_and_length_of_list(func):
    """
    Run test cases for the function to calculate the length and sum of a list of numbers.

    Args:
        func (function): The function to test.

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

    # Helper function to handle the test result
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
    class TestSumAndLengthOfList(unittest.TestCase):

        # Hidden Cases
        def test_hidden_positive_integer_cases(self):
            inputs = [[random.randint(1, 500) for _ in range(random.randint(1, 20))] for _ in range(50)]
            expected = [(len(ip), sum(ip)) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])
        
        def test_hidden_mixed_integer_cases(self):
            inputs = [[random.randint(-500, 500) for _ in range(random.randint(1, 20))] for _ in range(40)]
            expected = [(len(ip), sum(ip)) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])
        
        # Open Test Cases
        def test_open_cases(self):
            inputs = [[random.randint(-500, 1000) for _ in range(random.randint(1,7))] for _ in range(5)]
            expected = [(len(ip), sum(ip)) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        
        def test_open_cases_float(self):
            inputs = [[random.uniform(-500, 1000) for _ in range(random.randint(1, 7))] for _ in range(2)]
            expected = [(len(ip), sum(ip)) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        
        # Test empty list
        def test_empty_list(self):
            inputs = []
            expected = (0, 0)
            result = func(inputs)
            handle_test_result(inputs, expected, result)
        
        # Test with zero
        def test_zero_list(self):
            inputs = [0, 0, 0, 0]
            expected = (4, 0)
            result = func(inputs)
            handle_test_result(inputs, expected, result)
        # Test not a list
        def test_not_a_list(self):
            inputs = "not a list"
            expected = (None, None)
            result = func(inputs)
            handle_test_result(inputs, expected, result)


        

    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSumAndLengthOfList)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_cases_sum_and_length_of_list(
        list_length_and_sum)

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
