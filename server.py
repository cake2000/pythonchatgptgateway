from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from openai import OpenAI
import uvicorn

# Initialize FastAPI app
app = FastAPI()

# Initialize OpenAI client with your API key from the OpenAI dashboard
client = OpenAI(api_key="sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# Define data models
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    model: str = "gpt-4o"

# Chat endpoint
@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        # Define the system message to enforce K-12 appropriateness
        system_message = {
            "role": "system",
            "content": "Make sure your responses are appropriate for K-12 schools, and reject any inappropriate requests."
        }
        # Prepend the system message to the client's messages
        messages = [system_message] + [msg.model_dump() for msg in request.messages]
        
        # Call the OpenAI API
        completion = client.chat.completions.create(
            model=request.model,
            messages=messages
        )
        
        assistant_message = completion.choices[0].message
        print(f"Assistant message: {assistant_message}")
        return {"role": assistant_message.role, "content": assistant_message.content}
    except Exception as e:
        # Debug: Print the exception
        print(f"Exception: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)