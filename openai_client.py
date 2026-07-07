from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()


class OpenAIClient(OpenAI):

    """
        This class is a wrapper around the OpenAI client, which is responsible for making API calls to generate responses based on the provided prompts. 
        It inherits from the OpenAI class and initializes the client with the API key from the environment variables.
    """

    def __init__(self):
        super().__init__(api_key=os.getenv("OPENAI_API_KEY")) # Call the parent class constructor to initialize the client with the API key