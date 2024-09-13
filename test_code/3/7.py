# Given a list of integers and another integer, return the index of this given integer.

import unittest
import random

# Run test cases
def run_test_find_index(func):
    """
    Run test cases for the function to check if it returns the correct index.

    Args:
    func (function): The find_index function to test.

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
    class TestFindIndex(unittest.TestCase):
        # Hidden Test Cases
        def test_hidden_integer_cases(self):
            inputs = [(ip, random.choice(ip)) for ip in [[random.randint(-1000,1000) for _ in range(random.randint(1,20))] for _ in range(45)]]
            expected = [ip[0].index(ip[1]) for ip in inputs]
            results = [func(ip[0], ip[1]) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        def test_hidden_float_cases(self):
            inputs = [(ip, random.choice(ip)) for ip in [[random.uniform(-1000,1000) for _ in range(random.randint(1,20))] for _ in range(45)]]
            expected = [ip[0].index(ip[1]) for ip in inputs]
            results = [func(ip[0], ip[1]) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])
        # Open Test Cases
        def test_integer_cases_not_in_list(self):
            inputs = [([random.randint(-1000, 1000) for _ in range(random.randint(1, 7))], random.uniform(-1000, 1000)) for _ in range(4)]
            expected = [-1] * len(inputs)
            results = [func(ip[0], ip[1]) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        def test_open_integer_cases(self):
            inputs = [(ip, random.choice(ip)) for ip in [[random.randint(-1000,1000) for _ in range(random.randint(1,7))] for _ in range(5)]]
            expected = [ip[0].index(ip[1]) for ip in inputs]
            results = [func(ip[0], ip[1]) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        def test_empty_list(self):
            inputs = [([], random.randint(-1000, 1000))]
            expected = [-1]
            results = [func(ip[0], ip[1]) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])


    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFindIndex)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return (
        successful_inputs,
        failed_inputs,
        successful_hidden_inputs,
        failed_hidden_inputs,
    )


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_find_index(find_index)

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
