# Given a list of integers, return the count of even numbers in it.
import unittest
import random

# Run Test Cases
def run_test_count_even_list(func):
    """
    Run test cases for the given function to calculate count of even numbers in a list

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

    # Helper functions to handle the test results
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
    class TestCountEvenList(unittest.TestCase):

        # Hidden Test Cases
        def test_hidden_cases1(self):
            inputs = [[random.randint(-100, 1000) for _ in range(random.randint(1, 20))] for _ in range(88)]
            count_even_list = lambda nums: len([num for num in nums if num % 2 == 0])
            expected = [count_even_list(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        # Open Test Cases
        def test_open_cases(self):
            inputs = [[random.randint(-10000,10000) for _ in range(random.randint(1,7))] for _ in range(10)]
            count_even_list = lambda nums: len([num for num in nums if num % 2 == 0])
            expected = [count_even_list(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        
        def test_empty_list(self):
            inputs = []
            expected = 0
            result = func(inputs)
            handle_test_result(inputs, expected, result)
        def test_list_with_zeros(self):
            inputs = [0, 0, 0]
            expected = 3
            result = func(inputs)
            handle_test_result(inputs, expected, result)





    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCountEvenList)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_count_even_list(
        count_even)

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