# Given a list of numbers, return the list in reverse order (without using list splicing).
import unittest
import random

# Run Test Cases
def run_test_reverse_list(func):
    """
    Run test cases for the given function to check if it reverses a list correctly.

    Args:
        func (function): The function to test.

    Returns:
        successful_inputs (list): A list of successful test cases.
        failed_inputs (list): A list of failed test cases.
        successful_hidden_inputs (list): A list of successful hidden test cases.
        failed_hidden_inputs (list): A list of failed hidden test cases.
    """
    successful_hidden_inputs = []
    failed_hidden_inputs = []
    successful_inputs = []
    failed_inputs = []

    # Helper functions
    def handle_hidden_test_result(inputs, expected, result):
        if expected == result:
            successful_hidden_inputs.append(inputs)
        else:
            failed_hidden_inputs.append(inputs)
    
    def handle_test_result(inputs, expected, result):
        if expected == result:
            successful_inputs.append(inputs)
        else:
            failed_inputs.append(inputs)


    # Test cases
    class TestReverseList(unittest.TestCase):

        # Hidden Test Cases
        def test_hidden_cases(self):
            inputs = [[random.randint(-1000,1000) for _ in range(random.randint(1,20))] for _ in range(90)]
            expected = [ip[::-1] for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])
                
        # Open Test Cases
        def test_open_cases(self):
            inputs = [[random.randint(-100, 100) for _ in range(random.randint(0,5))] for _ in range(10)]
            expected = [ip[::-1] for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])


    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseList)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_reverse_list(
        reverse_list)

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