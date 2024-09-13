# Given a list of integers, sort it on your own and return the median.

import unittest
import random
from statistics import median

def run_test_find_median(func):
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

        
    class TestFindMedian(unittest.TestCase):
        # Hidden Cases
        def test_6hidden_integer_cases(self):
            inputs = [[random.randint(-1000,1000) for _ in range(random.randint(1,70))] for _ in range(55)]
            expected = [median(ip) for ip in inputs]
            result = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], result[i])

        def test_7hidden_float_cases(self):
            inputs = [[round(random.uniform(-1000.0, 1000.0), 3) for _ in range(random.randint(1, 70))] for _ in range(35)]
            expected = [median(ip) for ip in inputs]
            result = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], result[i])

        # Open Cases

        def test_1empty_list(self):
            inputs = []
            expected = None
            result = func(inputs)
            handle_test_result(inputs, expected, result)

        def test_2single_element(self):
            inputs = [[random.randint(1,100)] for _ in range(2)]
            expected = [median(ip) for ip in inputs]
            result = [func(ip) for ip in inputs]
            handle_test_result(inputs, expected, result)

        def test_3zero_list(self):
            inputs = [0,0,0,0,0,0,-5,7,3]
            expected = median(inputs)
            result = func(inputs)
            handle_test_result(inputs, expected, result)

        def test_4multiple_elements(self):
            inputs = [[random.randint(-100,100) for _ in range(random.randint(1,10))] for _ in range(3)]
            expected = [median(ip) for ip in inputs]
            result = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], result[i])
        
        def test_5multiple_float_elements(self):
            inputs = [[round(random.uniform(-100.0, 100.0),3) for _ in range(random.randint(1, 10))] for _ in range(4)]
            expected = [median(ip) for ip in inputs]
            result = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], result[i])



    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFindMedian)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_find_median(sort_and_find_median)

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