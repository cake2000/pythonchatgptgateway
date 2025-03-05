import requests

def call_chatgpt_server(messages, model="gpt-4o", server_url="http://localhost:8000/chat"):
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
        {"role": "user", "content": "How are you?"}
    ]
    try:
        # Replace 'server_ip' with the actual server IP or domain
        response = call_chatgpt_server(messages, server_url="http://localhost:8000/chat")
        print(response["content"]) 
    except Exception as e:
        print(f"Client error: {e}")