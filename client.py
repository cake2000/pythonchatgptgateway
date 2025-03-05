import requests

def call_chatgpt_server(messages, model="gpt-4o", server_url="http://server_ip:8000/chat"):
    """
    Send a request to the ChatGPT gateway server and return the assistant's response.
    
    Args:
        messages (list): List of dictionaries with 'role' and 'content' (e.g., 'user', 'assistant').
        model (str): The OpenAI model to use (default: "gpt-4o").
        server_url (str): URL of the server endpoint.
    
    Returns:
        dict: Response containing 'role' and 'content'.
    
    Raises:
        Exception: If the server returns an error.
    """
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "messages": messages,
        "model": model
    }
    response = requests.post(server_url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}, {response.text}")

# Example usage
if __name__ == "__main__":
    # Sample user message
    messages = [
        {"role": "user", "content": "Write a haiku about recursion in programming."}
    ]
    try:
        # Replace 'server_ip' with the actual server IP or domain
        response = call_chatgpt_server(messages, server_url="http://localhost:8000/chat")
        print(response["content"])  # Print the assistant's response
    except Exception as e:
        print(f"Client error: {e}")