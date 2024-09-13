# Given a list of lists of integers, return a list that is sorted based on the sum of each inner list.
#  Do not use any inbuilt function for sorting.

import unittest
import random

# Run Test Cases

def run_test_sort_by_inner_sum(func):
    successful_hidden_inputs = []
    failed_hidden_inputs = []
    successful_inputs = []
    failed_inputs = []
    expected_outputs = []

    # Helper Functions to handle the test results
    def handle_hidden_test_result(inputs, expected, result):
        if expected == result:
            successful_hidden_inputs.append(inputs)
        else:
            failed_hidden_inputs.append(inputs)

    def handle_test_result(inputs, expected, result):
        if expected == result:
            successful_inputs.append((inputs))

        else:
            failed_inputs.append(inputs)

    # Test Cases
    class TestSortBySum(unittest.TestCase):
        # Hidden Cases
        def test_hidden_cases(self):
            inputs = [[[random.randint(-1000, 1000) for _ in range(random.randint(0, 12))]for _ in range(random.randint(0, 20))]for _ in range(47)]
            expected = [sort_by_inner_sum(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])
            
        def test_hidden_cases_2(self):
            inputs = [[[round(random.uniform(-1000, 1000),2) for _ in range(random.randint(0, 12))]for _ in range(random.randint(0, 20))]for _ in range(47)]
            expected = [sort_by_sum(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        # Open Cases
        def test_1empty_list(self):
            inputs = []
            print(f"TestCase 1 Inputs:  {inputs}")
            expected = []
            result = func(inputs)
            handle_test_result(inputs, expected, result)
            expected_outputs.append(expected)

        def test_2sorting_empty_list(self):
            inputs = [[],[],[random.randint(1,10) for _ in range(0,3)], [random.randint(0,4) for _ in range(0,5)], [],[]]
            expected = sort_by_inner_sum(inputs)
            result = func(inputs)
            handle_test_result(inputs, expected, result)
            expected_outputs.append(expected)
        
        def test_3sorting_negative_lists(self):
            inputs = [[[random.randint(-100,-1) for _ in range(random.randint(1, 6))]for _ in range(random.randint(1,6))]for _ in range(2)]           
            expected = [sort_by_inner_sum(ip) for ip in inputs]
            result = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], result[i])
            expected_outputs.append(expected)

        def test_4positive_lists(self):
            inputs = [[[random.randint(1, 100) for _ in range(random.randint(1, 6))]for _ in range(random.randint(1, 7))]for _ in range(2)]
            expected = [sort_by_inner_sum(ip) for ip in inputs]
            result = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], result[i])
            expected_outputs.append(expected)


    
    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSortBySum)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs, expected_outputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __, expected_outputs = run_test_sort_by_inner_sum(sort_by_sum)

    # Print Open Test Results
    print("Open Test Results:")
    print("TestCase Inputs:", successful_inputs)
    print("Expected Outputs:", expected_outputs)
    print("Failed Inputs:", failed_inputs)

    # Print Total Test Results
    print("Total Test Results:")
    print("Successful Inputs:", len(successful_inputs) + len(_))

    # Print Summary
    if len(failed_inputs) + len(__) == 0:
        print("All test cases passed!")
    else:
        print("Some test cases failed.")

