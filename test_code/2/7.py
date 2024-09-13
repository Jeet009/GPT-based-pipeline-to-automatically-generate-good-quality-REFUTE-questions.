# Given a binary representation of an integer (input using integer datatype),
#  return the corresponding integer value in decimal representation.

import unittest
import random

# Run test cases


def run_test_binary_to_decimal(func):
    """
    Run test cases for the given function to calculate equivalent decimal number of a given positive binary number in integer format.

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

    # Helper function to generate random binary numbers
    def generate_random_binary_list(size, min_value=0, max_value=1):
        """
        Generate a list of random binary numbers of size 'size' in integer format
        Each binary number is a  maximum of 12-bit number.
        Args:
            size (int): The size of the list to generate.
            min_value (int): The minimum value of each binary number. Default is 0.
            max_value (int): The maximum value of each binary number. Default is 1.
        Returns:
            binary_list (list): A list of random binary numbers in integer format.
        """
        binary_list = []
        for _ in range(size):
            binary_str = ''.join(str(random.randint(min_value, max_value))
                                 for _ in range(12))  # Assuming 12 bit binary numbers
            binary_list.append(int(binary_str))
        return binary_list

    # Test Cases
    class TestBinToDec(unittest.TestCase):
        # Hidden Test Cases
        def test_hidden_cases(self):
            inputs = generate_random_binary_list(70)
            expected = [bin_2_dec(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])
        # Open Test Cases

        def test_open_cases(self):
            inputs = generate_random_binary_list(20)
            expected = [bin_2_dec(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        # Negative Numbers

        def test_negative_numbers(self):
            inputs = [-1, -10, -11, -100, -101, -
                      110, -111, -1000, -1001, -1010]
            expected = [None] * len(inputs)
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
     # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBinToDec)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_binary_to_decimal(
        bin_2_dec)

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
