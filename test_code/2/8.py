# Given a positive integer, return True if its a palindrome, else return False.

import unittest
import random

# Run Test Cases


def run_test_check_palindrome(func):
    """
    Run test cases for the function to check a number is palindrome or not

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

    # Helper function to handle the test results
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

    # Helper function to generate random palindromes
    def generate_random_palindrome(num_palindromes, min_value, max_value):
        """
        Generate a list of random palindromes.

        Args:
            num_palindromes (int): The number of palindromes to generate.
            min_value (int): The minimum value of the palindromes.
            max_value (int): The maximum value of the palindromes.

        Returns:
            palindromes(list): A list of random palindrome numbers.
        """
        palindromes = []
        while len(palindromes) < num_palindromes:
            num = random.randint(min_value, max_value)
            num_str = str(num)
            if num_str == num_str[::-1]:
                palindromes.append(num)

        return palindromes

    # Test Cases
    class TestCheckPalindrome(unittest.TestCase):
        # Hidden Test cases positive
        def test_hidden_positive_cases(self):
            inputs = generate_random_palindrome(40, 10000, 999999)
            expected = [True] * len(inputs)
            results = [func(num) for num in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])
        # Hidden Test cases for Random numbers

        def test_hidden_random_cases(self):
            inputs = [random.randint(0, 999999) for _ in range(40)]
            expected = [is_palindrome(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        # Open Positive Test cases

        def test_open_positive_cases(self):
            inputs = generate_random_palindrome(10, 100, 9999)
            expected = [True] * len(inputs)
            results = [func(num) for num in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        # Open Negative Test cases

        def test_negative_cases(self):
            inputs = [random.randint(-9999, -1) for _ in range(10)]
            expected = [False] * len(inputs)
            results = [func(num) for num in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])

    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCheckPalindrome)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_check_palindrome(
        is_palindrome)

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
