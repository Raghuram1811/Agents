class Response:

    """
        This class is responsible for generating responses from the OpenAI API.
        It takes a client instance as an argument and uses it to make API calls in the response method.
    """

    def __init__(self, client):
        self._client = client # Store the client instance for later use in the response method
    
    def response(self, prompt=None):
        response = self._client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        return response