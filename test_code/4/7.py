# Given two 2D matrices of the same dimensions, return their sum.
import unittest
import random
import numpy as np

# Run Test Cases
def run_test_sum_matrices(func):
    successful_hidden_inputs = []
    failed_hidden_inputs = []
    successful_inputs = []
    failed_inputs = []

    # Helper Functions to handle the test results
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

    # Helper Functions to generate matrices
    def generate_same_D_matrix(nums,rows, cols):
        matrix_pairs = []
        for _ in range(nums):
            matrix1 = np.random.randint(-100, 100, (rows, cols))
            matrix2 = np.random.randint(-100, 100, (rows, cols))
            matrix_pairs.append((matrix1, matrix2))
        return matrix_pairs

    def generate_different_D_ER_matrix(nums, rows, cols):
        matrix_pairs = []
        for _ in range(nums):
            matrix1 = np.random.randint(-10, 10, (rows, cols))
            matrix2 = np.random.randint(-10, 10, (rows+1, cols))
            matrix_pairs.append((matrix1, matrix2))
        return matrix_pairs
    def generate_different_D_EC_matrix(nums, rows, cols):
        matrix_pairs = []
        for _ in range(nums):
            matrix1 = np.random.randint(-10, 10, (rows, cols))
            matrix2 = np.random.randint(-10, 10, (rows, cols+1))
            matrix_pairs.append((matrix1, matrix2))
        return matrix_pairs

    # Test Cases
    class TestSumMatrices(unittest.TestCase):
        # Hidden Case
        def test_hidden_same_D_matrices(self):
            inputs = generate_same_D_matrix(50, 3, 2)
            expected = [sum_matrices(ip[0], ip[1]) for ip in inputs]
            result = [func(ip[0], ip[1]) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], result[i])

        def test_hidden_different_D_ER_matrices(self):
            inputs = generate_different_D_ER_matrix(20, 3, 2)
            expected = [sum_matrices(ip[0], ip[1]) for ip in inputs]
            result = [func(ip[0], ip[1]) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], result[i])
        
        def test_hidden_different_D_EC_matrices(self):
            inputs = generate_different_D_EC_matrix(25, 3, 2)
            expected = [sum_matrices(ip[0], ip[1]) for ip in inputs]
            result = [func(ip[0], ip[1]) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], result[i])




        # Open Cases
        def test_empty_matrices(self):
            matrix_a = []
            matrix_b = []
            expected = []
            result = func(matrix_a, matrix_b)
            handle_test_result((matrix_a, matrix_b), expected, result)
        def test_empty_nested_matrices(self):
            matrix_a = [[]]
            matrix_b = [[]]
            expected = [[]]
            result = func(matrix_a, matrix_b)
            handle_test_result((matrix_a, matrix_b), expected, result)
        
        def test_two_matrices(self):
            inputs = generate_same_D_matrix(1, 3, 2)
            expected = [sum_matrices(ip[0], ip[1]) for ip in inputs]
            result = [func(ip[0], ip[1]) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], result[i])
        
        def test_different_D_ER_matrices(self):
            inputs = generate_different_D_ER_matrix(1, 3, 2)
            expected = [sum_matrices(ip[0], ip[1]) for ip in inputs]
            result = [func(ip[0], ip[1]) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], result[i])
        
        def test_different_D_EC_matrices(self):
            inputs = generate_different_D_EC_matrix(1, 3, 2)
            expected = [sum_matrices(ip[0], ip[1]) for ip in inputs]
            result = [func(ip[0], ip[1]) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], result[i])
    



    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSumMatrices)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_sum_matrices(sum_matrices_base_case)

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







# print(sum_matrices([], []))  # Output: None
# print(sum_matrices([[]], [[]]))  # Output: None
# print(sum_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]))  # Output: [[6, 8], [10, 12]]
# print(sum_matrices([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]))  # Output: [[8, 10, 12], [14, 16, 18]]
# print(sum_matrices([[1, 2], [3, 4]], [[5, 6], [7]]))  # Output: None
# print(sum_matrices([[1, 2], [3]], [[5, 6], [7, 8]]))  # Output: None
