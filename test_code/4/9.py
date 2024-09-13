# Given a list of integers, return its mode (list of numbers with highest frequency of occurrence). 
# Do not use a dictionary.

import unittest
import random
from statistics import multimode




def run_test_find_mode(func):
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

    # Helper functions to generate random list for test cases
    def generate_int_data(length): # Generates list with repeating 1 random integer from the list

        # Generate a list of random integers
        random_list = [random.randint(-100, 100) for _ in range(length)]
        #choose random numbers to repeat
        repeat_numbers = random.sample(random_list, random.randint(1,length))

        # Repeat the number occurances and add the to the list
        for num in repeat_numbers:
            while random_list.count(num) < random.randint(1,random.randint(1, length)):
                # Generate a random index to insert the reapeat_number
                random_index = random.randint(0, len(random_list))
                random_list.insert(random_index, num)

        return random_list

    # Helper functions to genererate random list for test cases
    def generate_float_data(length): # Generates list with repeating 1 random integer from the list

        # Generate a list of random integers
        random_list = [round(random.uniform(-100, 100),3) for _ in range(length)]
        # choose random numbers to repeat
        repeat_numbers = random.sample(random_list, random.randint(1,length))

        # Repeat the number occurances and add the to the list
        for num in repeat_numbers:
            while random_list.count(num) < random.randint(1,random.randint(1, length)):
                # Generate a random index to insert the reapeat_number
                random_index = random.randint(0, len(random_list))
                random_list.insert(random_index, num)

        return random_list

    class TestFindMode(unittest.TestCase):

        #Hidden Cases
        def test_hidden_int_cases(self):
            inputs = [generate_int_data(random.randint(20,100)) for _ in range(45)]
            expected = [multimode(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])
        def test_hidden_float_cases(self):
            inputs = [generate_float_data(random.randint(20, 100)) for _ in range(45)]
            expected = [multimode(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_hidden_test_result(inputs[i], expected[i], results[i])

        # Open Cases
        def test_empty_list(self):
            inputs = []
            expected = []
            result = func(inputs)
            handle_test_result(inputs, expected, result)

        def test_single_element(self):
            inputs = [[random.randint(-10,10)] for _ in range(4)]
            expected = [multimode(ip) for ip in inputs]
            result = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], result[i])
        def test_integer_cases(self):
            inputs = [generate_int_data(12) for _ in range(3)]
            expected = [multimode(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
           
        def test_float_cases(self):
            inputs = [generate_float_data(12) for _ in range(2)]
            expected = [multimode(ip) for ip in inputs]
            results = [func(ip) for ip in inputs]
            for i in range(len(inputs)):
                handle_test_result(inputs[i], expected[i], results[i])
        # # def

    # create Test Suite for the function
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFindMode)
    # run Test Suite
    final = unittest.TextTestRunner().run(suite)

    return successful_inputs, failed_inputs, successful_hidden_inputs, failed_hidden_inputs


if __name__ == "__main__":
    successful_inputs, failed_inputs, _, __ = run_test_find_mode(find_mode)

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





