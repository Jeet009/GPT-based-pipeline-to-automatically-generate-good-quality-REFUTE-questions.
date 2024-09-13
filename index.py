# Using class method 

import requests
import json
import gradio as gr
from openai import OpenAI

import unittest
import random

class Pytutor:
    # Constructor 
    def __init__(self, model):
        self.url="http://localhost:11434/api/generate"
        self.headers={'Content-Type':'application/json'   }
        self.model = model
        self.res = None
        self.gpt = None


    # Function to get user input
    def user_input(self):
        problems = open('problems.json')
        concepts = json.load(problems)

        for i in concepts:
            print("Concept " + str(i['concept']) + ": " + i['title'])

        concept_no = input('Choose your concept number : ')
        print(f"******** LIST OF PROGRAMS FOR CONCEPT NO {concept_no} ********")

        for i in concepts:
            if (int(concept_no) == int(i['concept'])):
                for j in i['questions']:
                    print("Program " + str(j['number']) + ": " + j['text'])
                    print(" ")
                       
        program_no = input('Choose your program number : ')
        print("*** THE PROGRAM ***")

        for i in concepts:
            if (int(concept_no) == int(i['concept'])):
                for j in i['questions']:
                    if (int(program_no) == int(j['number'])):
                        print("Program " + str(j['number']) + ": " + j['text'])
                        self.prompt = j['text']
                        self.function_name = j['function_name']
        
        self.res = self.generate_response(self.prompt, self.function_name)
        print(self.res)
        self.gpt = input("Use GPT 4o : Type y for YES or n for NO : ")
        if(self.gpt == "y"):
            # Use GPT4 model to test program and run test cases
            self.gpt_four_code()
        else:
            # In case of stable code, extracting it's code using codellama
            if(self.model == "stable-code:latest"):
                data={
                    "model": "codellama:latest",
                    "prompt":f"Extract the code from the {self.res} and return only the code for the function without any description or preamble.",
                    "stream":False
                }
                response=requests.post(self.url,headers=self.headers,data=json.dumps(data))

                if response.status_code==200:
                    response=response.text
                    data=json.loads(response)
                    actual_response=data['response']
                    self.res = actual_response
                else:
                    print("error:",response.text)

            print("Extracted Code")
            print(self.res)
            self.file_operation(self.res, concept_no, program_no)

    #Function to use GPT4 model to test program and run test cases
    def gpt_four_code(self):
        client = OpenAI()
        completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a tester. You create all possible test cases to test the given code."},
            {
                "role": "user",
                "content": f"Test given program with test cases. {self.res}. Try edge cases also.",
            }
        ]
        )       
        print(completion.choices[0].message)    

    # Function to handle file operations
    def file_operation(self, res, c_no, p_no):
        print("Performing operations on temp file ...")
        # print(res)
        # Writing respose to temp file 
        # f = open('temp.py', 'w')
        # f.writelines(res[3:len(res)-4])
        # f.close()
        if self.model == 'codellama:7b':
            f = open('temp.py', 'w')
            f.writelines(res[3:len(res)-4])
            f.close()
        elif self.model == 'stable-code:latest':
            f = open('temp.py', 'w')
            f.writelines(res[3:len(res)-4])
            f.close()
            
                # f.writelines(res[5:len(res)-4])
                # f.close()

        # Appending test code to temp file 
        temp_file = open('temp.py', 'a')
        read_file = open(f'test_code/{c_no}/{p_no}.py', 'r')
        temp_file.write('\n')
        temp_file.writelines(read_file)
        temp_file.close()

        # Executing temp file 
        print('Executing temp file ...')
        exec(open('temp.py').read())

    # Function to generate response from llm
    def generate_response(self, prompt, func_name):
        # history.append(prompt)
        # final_prompt="\n".join(history)
        if (self.model == "codellama:7b"):
            data={
                "model":self.model,
                "prompt":f"Write a python program for {prompt} with function name {func_name}. Complete the program in itself. Return only the code as output. Do not give explaination",
                "stream":False
            }
        elif(self.model == "stable-code:latest"):
            data={
                "model":self.model,
                "prompt":f"Write a python function for {prompt} with function name {func_name}. Return only the code for the function as output. Do not add any explaination in the end or beginning. Do not add preamble. Remember, return only the code",
                "stream":False
            }

        response=requests.post(self.url,headers=self.headers,data=json.dumps(data))

        if response.status_code==200:
            response=response.text
            data=json.loads(response)
            actual_response=data['response']
            return actual_response
        else:
            print("error:",response.text)


print("""
      1: codellama:7b
      2: stable-code:latest
      """)
model = input("Choose language model to generate program : ")
if int(model) == 1:
    p = Pytutor("codellama:7b")
    p.user_input()
elif int(model) == 2:
    q = Pytutor("stable-code:latest")
    q.user_input()

