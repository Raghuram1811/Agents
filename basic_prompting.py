from openai_client import OpenAIClient
from response import Response

"""
    This file contains the implementation of different prompting techniques for generating responses from the OpenAI API.
    The Response class is defined in response.py and is responsible for making API calls to generate responses based on the provided prompts. The ChainOfThoughts and MultiShotPrompting classes inherit from the Response
    class and implement specific prompting techniques for generating responses. The main function demonstrates how to use these classes to generate responses based on different prompting techniques.  
"""

class ChainOfThoughts(Response):

    """
        This class implements the Chain of Thoughts prompting technique, which encourages the model to think step-by-step when generating responses. 
        It inherits from the Response class and uses the response method to generate responses based on the provided prompts. The ask method generates a response for a single prompt, while the ask_fewshot method provides multiple examples in the prompt to encourage step-by-step thinking.
    """

    def __init__(self, client):
        super().__init__(client) # Call the parent class constructor to initialize the client

    def ask(self, prompt=None):
        prompt = "Lets think step by step, what is the value of x if x + 2 = 5?" if not prompt else prompt
        response = self.response(prompt)
        return response.choices[0].message.content
    
    def ask_fewshot(self, prompt=None):
        prompt = """
        Solve these word problems step-by-step:

        Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls.
        Each can has 3 tennis balls. How many tennis balls does he have now?
        A: Roger started with 5 balls.
        Step 1: He bought 2 cans, each with 3 balls: 2 * 3 = 6 balls
        Step 2: Add to his original: 5 + 6 = 11 balls
        Answer: 11 tennis balls

        Q: The cafeteria had 23 apples. If they used 20 to make lunch and
        bought 6 more, how many apples do they have?
        A: Started with 23 apples.
        Step 1: Used 20 for lunch: 23 - 20 = 3 apples left
        Step 2: Bought 6 more: 3 + 6 = 9 apples
        Answer: 9 apples

        Q: A parking lot has 12 spaces. 8 are occupied. 3 cars leave and
        5 new cars arrive. How many spaces are now occupied?
        A:
        """ 
        prompt = None if not prompt else prompt
        response = self.response(prompt)
        return response.choices[0].message.content
    
class MultiShotPrompting(Response):

    """
        This class implements the Multi-Shot Prompting technique, which provides multiple examples in the prompt to guide the model's response generation. 
        It inherits from the Response class and uses the response method to generate responses based on the provided prompts.
    """

    def __init__(self, client):
        super().__init__(client) # call the parent class constructor to initialize the client
        
    def ask(self, prompt=None, shot=0):
        ##### Simulate the multi-shot prompting by providing a few examples in the prompt itself #####
        if shot>=2:
            prompt = """You are a helpful assistant that provides concise answers to questions. 
            Here are some examples of how you answer questions:
            Q: What is the capital of France?
            A: The capital of France is Paris.
            Q: Who wrote 'To Kill a Mockingbird'?
            A: 'To Kill a Mockingbird' was written by Harper Lee.
            Now, please answer the following question:
            Q: A bat and a ball cost $1.10 in total.
                The bat costs $1.00 more than the ball.
                How much does the ball cost?""" if not prompt else prompt
        
        elif shot==1:
            prompt = """You are a helpful assistant that provides concise answers to questions. 
            Here is an example of how you answer questions:
            Q: What is the capital of France?
            A: The capital of France is Paris.
            Now, please answer the following question:
            Q: What is the largest mammal?""" if not prompt else prompt
        
        else:
            prompt = "What is the largest mammal?" if not prompt else prompt
        
        response = self.response(prompt)
        return response.choices[0].message.content

def main():
    client = OpenAIClient()
    response = MultiShotPrompting(client=client).ask(shot=2) # Change the shot value to 0, 1, or 2 to see the effect of multi-shot prompting

    response = ChainOfThoughts(client=client).ask_fewshot() # Example of chain of thoughts prompting
    print(response)

if __name__ == "__main__":
    main()